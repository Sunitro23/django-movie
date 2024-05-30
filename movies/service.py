import os
import logging
from typing import List, Union
from dotenv import load_dotenv
import requests
from movies.models import Movie

load_dotenv()
api_key = os.getenv("API_KEY")


def get_data_from_api(endpoint: str, title: str) -> Union[List[dict], dict]:
    url = f"https://www.omdbapi.com/?{endpoint}={title}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        if endpoint == "s":
            return response.json()["Search"]
        else:
            return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request to {url} failed: {e}")
        return [] if endpoint == "s" else {}


def get_movies(title: str) -> List[Movie]:
    try:
        db_movies = Movie.objects.filter(title__icontains=title)
        if not db_movies:
            movies = get_data_from_api("s", title)
            movies_detailed: List[Movie] = []
            for movie in movies:
                movie_data = get_data_from_api("t", movie["Title"])
                if movie_data:
                    movie: Movie = save_movie_to_db(movie_data)
                    movies_detailed.append(movie)
            return movies_detailed
        return list(db_movies)
    except Exception as e:
        logging.error(f"An error occurred while retrieving movies: {e}")
        return []


def get_movie(id: int) -> Movie:
    try:
        movie = Movie.objects.get(id=id)
        return movie
    except Exception as e:
        logging.error(f"An error occurred while retrieving movie: {e}")
        return None


def save_movie_to_db(movie_data: dict) -> Movie:
    try:
        if movie_data:
            movie: Movie = Movie.objects.create(
                title=movie_data["Title"],
                year=movie_data["Year"],
                poster=movie_data["Poster"],
                plot=movie_data["Plot"],
            )
            movie.set_genre(movie_data["Genre"])
            movie.save()
            return movie
        else:
            return None
    except Exception as e:
        logging.error(f"An error occurred while saving movie to the database: {e}")
        return None
