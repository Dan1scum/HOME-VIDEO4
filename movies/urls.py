from django.urls import path
from .views import movie_list, MovieCreateView, movie_detail

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:id>/', movie_detail, name='movie_detail'),
]
