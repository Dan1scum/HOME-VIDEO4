from django.urls import path
from .views import movie_list, movie_create

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('create/', movie_create, name='movie_create'),
]
