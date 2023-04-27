from django.shortcuts import render
from django.http import HttpResponse
import json
from todo.models import *
from todo.forms import *

def display_todos(request):
    a=Todo.objects.all()
    context={"header": "All tasks", "message": a}
    return render(request, 'index.html', context)

def todo(request):
    
    if request.method=='POST':
        form=Todo_new(request.POST)
        form.save()
        print("The task edded")
    
    context = {
        'form' : Todo_new()
    }
    return render(request, 'todo.html', context)

def todo_done(request, todo_id):
    a=Todo.objects.get(id=todo_id)
    context={"header": a.title, "message": a}
    return render(request, 'todo_done.html', context)


    # if request.GET:
    #     done = request.GET['geeks_field']
    #     print(temp)