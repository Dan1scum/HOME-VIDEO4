from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movie/<int:id>/', movie_detail, name='movie_detail'),
]