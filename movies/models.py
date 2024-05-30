import datetime
from django.db import models


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __to_dict__(self):
        return {"name": self.name}


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    year = models.CharField(help_text="Release year", max_length=100)
    genre = models.ManyToManyField(Genre, blank=True)
    poster = models.URLField(max_length=200, default="https://via.placeholder.com/150")
    plot = models.TextField(blank=True)

    def __str__(self):
        str = f"{self.title} {self.year} {self.poster}"
        str += f' - {", ".join([genre.name for genre in self.genre.all()])}'
        return str

    def __to_dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": [genre.__to_dict__ for genre in self.genre.all()],
            "poster": self.poster,
            "plot": self.plot,
        }

    def set_genre(self, genre):
        genre_array = genre.split(",")
        for genre_name in genre_array:
            genre_obj, _ = Genre.objects.get_or_create(name=genre_name)
            self.genre.add(genre_obj.id)
