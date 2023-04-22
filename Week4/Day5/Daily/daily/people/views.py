from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
import json
info = [
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
info.sort(key=lambda d: d['age']) 


def index(request):
    context={"header": "People", "message": info}
    return render(request, 'index.html', context)

def people(request, person_id):
    for s in info:
        if s['id']==person_id: 
            pers=s  
            break
    context={"header": s['name'], "message": pers}
    return render(request, 'people.html', context)

