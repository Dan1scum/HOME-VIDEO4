from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Create your views here.