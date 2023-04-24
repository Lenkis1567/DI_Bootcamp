from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('family/<int:family_id>', views.family),
	path('animals/', views.animals),
    path('animal/<int:animal_id>', views.animal)

]