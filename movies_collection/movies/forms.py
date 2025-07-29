<<<<<<< HEAD
from django import forms
from .models import Genre, Director, Movie



class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'birth_date', 'nationality']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'release_year',
            'genre',
            'director',
            'description',
            'poster',
            'watched',

        ]
=======
from django import forms
from .models import Genre, Director, Movie

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'birth_date', 'nationality']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'release_year',
            'genre',
            'director',
            'description',
            'poster',
            'watched'
        ]
>>>>>>> 4f68607c009084eaff717179e7c65302565faca6
