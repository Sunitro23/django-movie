from asyncio import Future
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from movies.service import get_movie_by_id_db, get_movies_by_title_db


def index(request):
    return render(request, "index.html")


def movie_page(request, movie_id):
    try:
        get_movies_by_title_db("Star Wars")
        movie = get_movie_by_id_db(movie_id)
    except Movie.DoesNotExist:
        movie = None
    if movie:
        return render(request, "movie_page.html", {"movie": movie})
    else:
        return HttpResponse("No movie found.")
