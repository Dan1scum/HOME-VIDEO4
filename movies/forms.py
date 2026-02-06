from django import forms
from django.forms import CheckboxSelectMultiple
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image', 'genres']
        widgets = {
            'genres': CheckboxSelectMultiple(),
        }
