from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('homepage', views.films),
    path('add_film', views.add_film),
    path('add_director', views.add_director)
]

