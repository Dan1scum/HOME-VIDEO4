from django.urls import path
from .views import genre_list, genre_detail

urlpatterns = [
    path('', genre_list, name='genre_list'),
    path('<int:id>/', genre_detail, name='genre_detail'),
]