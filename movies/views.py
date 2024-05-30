from asyncio import Future
from typing import List
from django.http import HttpResponse

from movies.models import Movie
from .forms import MovieForm
from django.shortcuts import render
from movies.service import (
    get_movie,
    get_movies,
)


def index(request):
    if request.method == "GET":
        context = {"form": MovieForm()}
        return render(request, "index.html", context)
    elif request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            title = form.cleaned_data["title"]
            movies: List[Movie] = get_movies(title)
            return get_movies_search(request, movies)
    else:
        return HttpResponse("Erreur")


def get_movies_search(request, movies):
    if movies is None:
        return HttpResponse("No movies found")
    return render(request, "movies.html", {"movies": movies, "form": MovieForm()})


def movie_page(request, movie_id):
    movie = get_movie(movie_id)
    print(movie)
    if movie:
        return render(request, "movie_page.html", {"movie": movie, "form": MovieForm()})
    else:
        return HttpResponse("No movie found.")
