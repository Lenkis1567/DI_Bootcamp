from django.contrib import admin
from .models import Customer, Vehicle_type, Vehicle_size, Vehicle, Rental, Rental_Rate

admin.site.register(Customer)
admin.site.register(Vehicle_type)
admin.site.register(Vehicle_size)
admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(Rental_Rate)
