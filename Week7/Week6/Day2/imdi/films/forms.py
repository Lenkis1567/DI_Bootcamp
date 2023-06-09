from django import forms
from .models import Country, Director, Film, Category
from django.forms.widgets import NumberInput  

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name')

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'release_date', 'created_in_country', 'available_in_countries', 'category_v', 'director_v')
        widgets = {'release_date': NumberInput(attrs={'type':'date'})}
        labels = {'category_v': 'Category',
                  'director_v': "Director"}
        



        