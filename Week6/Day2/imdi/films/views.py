from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Country, Director, Film, Category
from .forms import DirectorForm, FilmForm
import json
from datetime import date
from django.views.decorators.http import require_GET, require_POST



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
            return redirect('/homepage')

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
            return redirect('/homepage')

    return render(request, 'add_director.html', context)


def edit_director(request, pk):
    director=Director.objects.get(id=pk)
    director_form = DirectorForm(instance=director)
    if request.method == "GET":
        context={"header": "Edit info about the director", "form": director_form}
        return render(request, 'add_director.html', context)
    
    if request.method =="POST":
        director_filled_form=DirectorForm(request.POST, instance=director)
        print(director_filled_form)
        if director_filled_form.is_valid():
            director_filled_form.save()
        return redirect('/homepage')


