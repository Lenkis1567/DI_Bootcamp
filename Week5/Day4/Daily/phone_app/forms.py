from django import forms
from .models import Person, Profile, Language

class PersonForm(forms.Form):
    class Meta:
        model = Person
        fields = ('name', 'phone_number')
        required = {'name': False}
        required = {'phone_number': False}

