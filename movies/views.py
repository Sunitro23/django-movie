from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Movies
from .forms import MovieForm


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
        
    


class MovieFormView(CreateView):
    model = Movies
    fields = ['title', 'year', 'genre', 'poster']
    success_url = reverse_lazy('search')