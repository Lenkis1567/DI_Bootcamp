from django.shortcuts import render
from .models import Person
# Create your views here.


def search(model, value):

    result = None
    try:
        model_one = model.objects.get(name = value)
        result = model_one
    except model.DoesNotExist:
        pass
    try:
        model_one = model.objects.get(phone_number = value)
        result = model_one
    except model.DoesNotExist:
        pass

    return result


def search_person(request, search_value: str):

    context = {}
    person_info = search(Person,  search_value)

    if person_info is not None:
        context = {'person': person_info}

    return render(request, 'person_info.html', context)


def profile_view(request, search_value: str):

    context = {}
    person_info = search(Person,  search_value)

    if person_info is not None:
        person_profile = person_info.profile
        profile_languages = person_profile.languages.all().order_by('name')
        context = {'person_info': person_info, 'person_profile': person_profile, 'languages': profile_languages}

    return render(request, 'profile.html', context)


def phonebook_view(request):
    persons = Person.objects.all().order_by('name')
    context={'person': persons}
    print (context)
    return render(request, 'phonebook.html', context)