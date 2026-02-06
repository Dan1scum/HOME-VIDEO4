from django.shortcuts import render, get_object_or_404
from .models import Genre
from movies.models import Movie

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre/genre_list.html', {'genres': genres})


def genre_detail(request, id):
    genre = get_object_or_404(Genre, id=id)
    movies = Movie.objects.filter(genres=genre)
    return render(request, 'genre/genre_detail.html', {'genre': genre, 'movies': movies})

# Create your views here.