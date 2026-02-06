from django.db import models
from genre.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    genres = models.ManyToManyField(Genre)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
