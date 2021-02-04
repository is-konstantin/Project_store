from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField("Name", max_length = 100)
    author_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.author_name

class Series(models.Model):
    series_name = models.CharField("Name", max_length = 100)
    series_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.series_name

class Genre(models.Model):
    genre_name = models.CharField("Name", max_length = 100)
    genre_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.genre_name

class Publishing_house(models.Model):
    publishing_house_name = models.CharField("Name", max_length = 100)
    publishing_house_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.publishing_house_name



