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
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
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
info["animals"].append({           
            "id" :4,
            "name": "Cow",
            "legs": 4,
            "weight": 800,
            "height":2,
            "speed": 30,
            "family": 3})
info["animals"].append({           
            "id" :5,
            "name": "Snake",
            "legs": 0,
            "weight": 0.2,
            "height":0.1,
            "speed": 10,
            "family": 4})
info["animals"].append({           
            "id" :6,
            "name": "Bee",
            "legs": 6,
            "weight": 0.01,
            "height":0.01,
            "speed": 32,
            "family": 5})

info["families"].append({'id':4, "name":'Reptile'})
info["families"].append({'id':3, "name":'Mammal'})
info["families"].append({'id':4, "name":'Reptile'})
info["families"].append({'id':5, "name":'Insect'})
info["families"].append({'id':6, "name":'Arachnid'})
info["families"].append({'id':6, "name":'Amphibian'})
# print(info)
# print(info['animals'])
all_fam=[]
a=info['families']
for b in range(0, len(a)):
    all_fam.append(a[b])
print(a)

def get_list_animals(an, family):
    list_animals=[]
    for i in an:
        if an[i]['family']==family:
            list_animals.append(an[i]['name'])
            return list_animals
an =info['animals']
get_list_animals(an, 3)