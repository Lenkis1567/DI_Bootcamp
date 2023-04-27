from django import forms
from .models import *

class Todo_new(forms.ModelForm):
    class Meta:
        model = Todo
        fields= ('title', 'details', 'deadline_date', 'category')
        widgets = {
            'deadline_date': forms.SelectDateWidget}
        labels = {
            "details": ("Full info")
            }







    