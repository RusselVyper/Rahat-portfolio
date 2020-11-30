from django.shortcuts import render, get_object_or_404
from .models import Video


def movies(request):
    film = Video.objects
    return render(request, 'films/movie.html', {'film': film})
