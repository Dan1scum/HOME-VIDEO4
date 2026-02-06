from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from genre.models import Genre

def movie_list(request):
    genre_id = request.GET.get('genre')

    movies = Movie.objects.all()
    genres = Genre.objects.all()

    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres
    })


def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'movies/movie_create.html', {'form': form})


# Create your views here.
