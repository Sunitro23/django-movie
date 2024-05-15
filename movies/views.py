from asyncio import Future
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Movies
from .forms import MovieForm
from django.shortcuts import render
from .models import Movie
from movies.service import get_movie_by_id_db, get_movies_by_title_db


def index(request):
    if request.method == "GET":
        form = MovieForm()
        context = {"form" : form}
        return render(request, 'index.html', context)
    elif request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        return HttpResponse("Erreur")
        
    
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


class MovieFormView(CreateView):
    model = Movies
    fields = ['title', 'year', 'genre', 'poster']
    success_url = reverse_lazy('search')