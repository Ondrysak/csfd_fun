from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

class Movie(models.Model):
    title = models.TextField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])



class Actor(models.Model):
    name = models.TextField(max_length=200)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])