from django.shortcuts import render
from .forms import AddGifForm

def add_gif(request):
    f = AddGifForm()
    context={

    }
    context['form']=f
    print (context)
    return render(request, 'add_gif.html', context)

def index(request):
    context='All gifs'
    return render(request, 'index.html', context)