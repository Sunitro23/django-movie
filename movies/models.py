import datetime
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    year = models.DateField(help_text="Release year")
    genres = models.ManyToManyField(Genre, blank=True)