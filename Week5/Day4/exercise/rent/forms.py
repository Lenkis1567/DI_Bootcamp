from django import forms
from .models import Customer, Vehicle, Rental, Vehicle_type, Vehicle_size, Rental_Rate

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country')

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
