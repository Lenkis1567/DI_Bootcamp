from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Director, Film, Category
from .forms import DirectorForm, FilmForm
import json
from datetime import date


def films(request):
    films_all=Film.objects.all()
    directors = []
    country_films = []
    categories =[]

    for film in films_all:  
        dir_film=film.director_v.all()
        country_film=film.available_in_countries.all()
        category=film.category_v.all()
        directors.append(dir_film)
        country_films.append(country_film)
        categories.append(category)

    all_films_dir = zip(films_all, directors, categories)
    print(all_films_dir)
    context={"header": "Films", "messages": all_films_dir}
    return render(request, 'homepage.html', context)

def add_film(request):
        
    if request.method == "GET":
        film_form = FilmForm()
        print ("Loading")
        context={"header": "Add a film", "form": film_form}
    
    if request.method =="POST":
        a=request.POST
        film_filled_form=FilmForm(request.POST)
        if film_filled_form.is_valid():
            film_filled_form.save()
            context={'header': 'Saved'}

    return render(request, 'add_film.html', context)

def add_director(request):
        
    if request.method == "GET":
        director_form = DirectorForm()
        print ("Loading")
        context={"header": "Add a director", "form": director_form}
    
    if request.method =="POST":
        a=request.POST
        director_filled_form=DirectorForm(request.POST)
        if director_filled_form.is_valid():
            director_filled_form.save()
            context={'header': 'Saved'}

    return render(request, 'add_director.html', context)