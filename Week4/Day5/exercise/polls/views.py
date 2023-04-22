from django.shortcuts import render
from django.http import HttpResponse
import json
info=people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


def index(request):
    listfamilies=info['families']
    context={"header": "Families", "message": listfamilies}
    return render(request, 'index.html', context)

def family(request, family_id):
    listanimals=list(filter(lambda x: x['family']==family_id, info['animals']))
    for s in info["families"]:
        if s["id"] == family_id:
            a=s['name']
            break
    a='Animals of '+a
    context={"header": a, "message": listanimals}
    return render(request, 'family.html', context)

def animal(request, animal_id):
    for an in info['animals']:
        if an['id']==animal_id:
            animal=an
            break
    context={"header": animal["name"], "message": animal}
    return render(request, 'animal.html', context)

def animals(request):
    listanimals=info['animals']
    context={"header": "All animals", "message": listanimals}
    return render(request, 'animals.html', context)