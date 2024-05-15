from urllib import request
from .models import Movie

# import API KEY
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


async def get_movies_by_title_db(title):
    if not Movie.objects.filter(title__icontains=title):
        for movie in get_movies_by_title_api(title):
            Movie.objects.create(
                title=movie.title,
                year=movie.year,
                genre=movie.genre,
                poster=movie.poster,
            )
    return Movie.objects.filter(title__icontains=title)


async def get_movie_by_id_db(movie_id):
    return Movie.objects.get(id=movie_id)


async def get_movies_by_title_api(title):
    url = f"https://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = request.get(url)
    if response.status_code == 200:
        movies = response.json()
        return [map_json_to_movie(movie) for movie in movies]
    else:
        return None


# async def get_movie_by_id_api(movie_id):
#     url = f"https://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
#     response = request.get(url)
#     if response.status_code == 200:
#         movie = response.json()
#         return map_json_to_movie(movie)
#     else:
#         return None


def map_json_to_movie(json):
    return Movie(
        title=json["Title"],
        year=json["Year"],
        genre=json["Genre"],
        poster=json["Poster"],
    )
