from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    courent_date=datetime.now()
    context = {'weather':'warm', 'courent_date':courent_date}
    
  
    return render(request, 'index.html', context)
