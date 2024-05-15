import datetime
from django.db import models


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField(help_text="Release year")
    genre = models.ManyToManyField(Genre, blank=True)
    poster = models.URLField(max_length=200, default="https://via.placeholder.com/150")

    def __str__(self):
        str = f"{self.title} {self.year} {self.poster}"
        str += f' - {", ".join([genre.name for genre in self.genre.all()])}'
        return str

    def add_genre(self, genre):
        self.genre.add(genre)
        return self
