from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('homepage', views.films),
    path('add_film', views.add_film),
    path('add_director', views.add_director),
    path('edit_film/<int:id>', views.edit_film, name='edit_film'),
    path('edit_director/<int:pk>', views.edit_director, name='edit_director')
]

