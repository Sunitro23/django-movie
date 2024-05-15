from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search', views.movies, name="search"),
    path("<int:movie_id>/", views.movie_page, name="movie_page"),
]
