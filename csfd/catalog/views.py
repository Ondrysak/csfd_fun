from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalog.forms import SearchForm

from .models import Actor, Movie

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_movies = Movie.objects.all().count()
    num_actors = Actor.objects.all().count()

    
    context = {
        'num_movies': num_movies,
        'num_actors': num_actors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)




class MovieListView(generic.ListView):
    model = Movie



class MovieDetailView(generic.DetailView):
    model = Movie



class ActorListView(generic.ListView):
    model = Actor



class ActorDetailView(generic.DetailView):
    model = Actor



def search(request):
   
    if request.method == 'POST':

        form = SearchForm(request.POST)

        if form.is_valid():
            query_string = form.cleaned_data['query']
            res_actors = Actor.objects.filter(name__icontains=query_string)
            res_movies = Movie.objects.filter(title__icontains=query_string)


    else:
        proposed_query = 'kek'
        form = SearchForm(initial={'query': proposed_query})
        res_actors = []
        res_movies = []

    context = {
        'form': form,
        'actor_results': res_actors,
        'movie_results': res_movies, 
    }

    return render(request, 'search.html', context)