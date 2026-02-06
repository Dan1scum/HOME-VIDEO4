from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Movie
from .forms import MovieForm
from genre.models import Genre

def movie_list(request):
    genre_id = request.GET.get('genre')
    q = request.GET.get('q')

    movies = Movie.objects.all()
    genres = Genre.objects.all()

    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    if q:
        movies = movies.filter(title__icontains=q)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres
    })


class MovieCreateView(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'movies/movie_create.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            messages.success(request, 'Фильм успешно создан.')
            return redirect('movie_detail', id=movie.id)
        messages.error(request, 'Пожалуйста, исправьте ошибки формы.')
        return render(request, 'movies/movie_create.html', {'form': form})


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


# Create your views here.
