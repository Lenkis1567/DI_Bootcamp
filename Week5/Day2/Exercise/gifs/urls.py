from django.urls import path
from . import views

urlpatterns = [
    path('add_gif/', views.add_gif),
    path('', views.index)
]