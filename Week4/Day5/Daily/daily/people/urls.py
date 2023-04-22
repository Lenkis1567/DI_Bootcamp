from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ),
    path('people/<int:person_id>', views.people, name='id')
]