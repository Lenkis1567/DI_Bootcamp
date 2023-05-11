from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from django.http import HttpResponse


def search_person(request):
    if request.method == "GET":
        search_form = PersonForm()
        print ("Loading")
        context={"header": "Search a person"}
        return render(request, 'search.html', context)
    
    if request.method =="POST":    
        name_inp=request.POST['field1']
        tel_inp=request.POST['field2']
        if name_inp !='':
            all_name=Person.objects.filter(name=name_inp)
            context={'results':all_name}
        elif tel_inp !='': 
            all_names=Person.objects.filter(phone_number=tel_inp)
            print(tel_inp)
            context={'results':all_names}  
        else:
            context={'results':{'The fields are empty':"all the fields are empty"}}  
        print(context['results'])
        if len(context['results'])>0:
            pass
        else:
            context={'results':{"No such person": "no such person"}}  

        return render(request, 'search.html', context)

# def profile_view(request, search_value: str):
    
#     context = {}
#     person_info = search(Person, search_value)

#     if person_info is not None:
#         person_profile = person_info.profile
#         profile_languages = person_profile.languages.all().order_by('name')
#         context = {'person_info': person_info, 'person_profile': person_profile, 'languages': profile_languages}

#     return render(request, 'profile.html', context)


def phonebook_view(request):
    persons = Person.objects.all().order_by('name')
    context={'person': persons}
    print (context)
    return render(request, 'phonebook.html', context)

