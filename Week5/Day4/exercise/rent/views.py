from django.shortcuts import render
from django.http import HttpResponse
import json
from rent.models import *
# from rent.forms import *

def rentals(request):
    a=Rental.objects.all()
    context={"header": "All rentals", "message": a}
    return render(request, 'index.html', context)

def customer(request, customer_id):
    a=Customer.objects.get(id=customer_id)
    b=Rental.objects.filter(customer=customer_id)
    context={"header": a.first_name+" "+a.last_name, "message1": a, "message2":b}
    return render(request, 'customer.html', context)

def rental(request, rental_id):
    a=Rental.objects.get(id=rental_id)
    context={"header": f'Rental # {a.id}', "message": a}
    return render(request, 'rental.html', context)

def customers(request):
    a=Customer.objects.all()
    context={"header": "All customers", "message": a}
    return render(request, 'customers_list.html', context)

def vehicles(request):
    a=Vehicle.objects.all()
    context={"header": "All vehicles", "message": a}
    return render(request, 'vehicles_list.html', context)

def vehicle(request, vehicle_id):
    a=Vehicle.objects.get(id=vehicle_id)
    context={"header": a.vehicle, "message": a}
    return render(request, 'vehicle.html', context)