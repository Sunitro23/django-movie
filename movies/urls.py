from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search', views.get_movies_search, name="search"),
    path("<int:movie_id>/", views.movie_page, name="movie_page"),
]
