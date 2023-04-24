from django.shortcuts import render
from django.http import HttpResponse
import json
from animals.models import *

def index(request):
    a=Family.objects.all()
    context={"header": "Families", "message": a}
    return render(request, 'index.html', context)

def family(request, family_id):
    animals_family = Animals.objects.filter(family=family_id)    
    context={"header": Family.objects.get(id=family_id), "message": animals_family}
    return render(request, 'family.html', context)

def animal(request, animal_id):
    animal=Animals.objects.get(id=animal_id)
    # for an in Animals.objects.all():
    #     if an[id]==animal_id:
    #         animal=an
    #         break
   
    context={'header': animal.name, 'message': animal}
    return render(request, 'animal.html', context)

def animals(request):
    listanimals=Animals.objects.all()
    context={"header": "All animals", "message": listanimals}
    return render(request, 'animals.html', context)