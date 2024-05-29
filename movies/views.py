from asyncio import Future
from django.http import HttpResponse
from .forms import MovieForm
from django.shortcuts import render
from movies.service import get_movie_by_id_db, get_movies_by_title_db, get_movies_by_title_api


def index(request):
    if request.method == "GET":
        form = MovieForm()
        context = {"form" : form}
        return render(request, 'index.html', context)
    elif request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=False)            
            title = form.cleaned_data['title']
            movies = get_movies_by_title_api(title)
            return getMovies(request, movies)
    else:
        return HttpResponse("Erreur")
    
def getMovies(request, movies):
    context = {'movies' : movies[0]}
    return render(request, 'movies.html', context)
        
    
def movie_page(request, movie_id):
    get_movies_by_title_db("Star Wars")
    movie = get_movie_by_id_db(movie_id)
    if movie:
        return render(request, "movie_page.html", {"movie": movie})
    else:
        return HttpResponse("No movie found.")