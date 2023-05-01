from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.rentals),
    path('customers/<int:customer_id>', views.customer),
    path('rentals/<int:rental_id>', views.rental),
    path('customers_list', views.customers),
    path('vehicles_list', views.vehicles),
    path('vehicles/<int:vehicle_id>', views.vehicle),
    path('customer_add', views.add_customer),
    path('vehicle_add', views.add_vehicle),
    path('rental_add', views.add_rental),
]