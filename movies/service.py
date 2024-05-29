import requests
from .models import Movie, Genre
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def get_movies_by_title_db(title):
    if not Movie.objects.filter(title__icontains=title):
        for movie in get_movies_by_title_api(title):
            movie.save()
    return Movie.objects.filter(title__icontains=title)


def add_genres_to_movie(movie: Movie, genres: list[Genre]):
    for genre in genres:
        movie.add_genre(genre)
    return movie


def get_movies_by_title_api(title):
    url = f"https://www.omdbapi.com/?s={title}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()        
        movie = json["Search"]
        return [map_json_to_movies(movie)]


def get_movie_by_id_db(movie_id):
    return Movie.objects.get(id=movie_id)


def map_json_to_movies(json):
    movies_list = []
    for search in json:
        movie = Movie(
            title=search['Title'],
            year=search['Year'],
            poster=search['Poster'],
        )
        movie.save()
        movies_list.append(movie)
    return movies_list


def map_json_to_movie(json):
    movie = Movie(
        title=json["Title"],
        year=json["Year"],
        poster=json["Poster"],
    )
    movie.save()
    add_genres_to_movie(movie, json["Genre"].split(", "))
    return movie


def add_genres_to_movie(movie: Movie, genres):
    for genre in genres:
        movie.add_genre(genre)
    return movie
