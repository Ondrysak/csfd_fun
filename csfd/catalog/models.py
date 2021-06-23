from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.postgres.indexes import GinIndex


from django.contrib.postgres.indexes import GinIndex

class UpperGinIndex(GinIndex):
    #  https://stackoverflow.com/posts/57038717/revisions
    def create_sql(self, model, schema_editor, using='', **kwargs):
        statement = super().create_sql(model, schema_editor, using=using, **kwargs)
        quote_name = statement.parts['columns'].quote_name

        def upper_quoted(column):
            return f'UPPER({quote_name(column)})'
        statement.parts['columns'].quote_name = upper_quoted
        return statement



class Movie(models.Model):
    title = models.TextField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])
    class Meta:
       indexes = [UpperGinIndex(name="movies_gin_trgm_idx", fields=("title",), opclasses=("gin_trgm_ops",))]





class Actor(models.Model):
    name = models.TextField(max_length=200)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])
    class Meta:
       indexes = [UpperGinIndex(name="actors_gin_trgm_idx", fields=("name",), opclasses=("gin_trgm_ops",))]