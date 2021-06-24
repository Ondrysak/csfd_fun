from django.urls import reverse
from django.test import TestCase
from catalog.models import Actor, Movie
from catalog.forms import SearchForm

# Create your tests here.


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        a = Actor.objects.create(name='Big Boy')
        m = Movie.objects.create(title='Super Movie')
        a.save()
        m.save()

    def test_get_actor_absolute_url(self):
        actor = Actor.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(actor.get_absolute_url(), '/catalog/actor/1')

    def test_get_movie_absolute_url(self):
        movie = Movie.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(movie.get_absolute_url(), '/catalog/movie/1')


class SearchFormTest(TestCase):
    def test_renew_form_date_field_help_text(self):
        form = SearchForm()
        self.assertEqual(form.fields['query'].help_text, 'enter your query!')





