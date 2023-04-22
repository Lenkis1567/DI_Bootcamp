from django.shortcuts import render
from django.http import HttpResponse
import json
info={
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2,
            "url": 'dog.webp'
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1,
            "url": 'panter.jpg' 
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1,
            "url": 'panter.jpg' 
        }
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
    ]
}
# anim_d = json.loads(info)
info["animals"].append({           
            "id" :4,
            "name": "Cow",
            "legs": 4,
            "weight": 800,
            "height":2,
            "speed": 30,
            "family": 3,
            "url": 'panter.jpg' })
info["animals"].append({           
            "id" :5,
            "name": "Snake",
            "legs": 0,
            "weight": 0.2,
            "height":0.1,
            "speed": 10,
            "family": 4,
            "url": 'panter.jpg' })
info["animals"].append({           
            "id" :6,
            "name": "Bee",
            "legs": 6,
            "weight": 0.01,
            "height":0.01,
            "speed": 32,
            "family": 5,
            "url": 'bee.jpg' })

info["families"].append({'id':4, "name":'Reptile'})
info["families"].append({'id':3, "name":'Mammal'})
info["families"].append({'id':5, "name":'Insect'})
info["families"].append({'id':6, "name":'Arachnid'})
info["families"].append({'id':7, "name":'Amphibian'})



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