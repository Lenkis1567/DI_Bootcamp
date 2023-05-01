from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm, VehicleForm, RentalForm
from .models import Customer, Vehicle, Rental
import json
from rent.models import *
from datetime import date

def rentals(request):
    a=Rental.objects.all().order_by('-return_date')
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
    a=Customer.objects.all().order_by('first_name')
    context={"header": "All customers", "message": a}
    return render(request, 'customers_list.html', context)

def vehicles(request):
    a=Vehicle.objects.all().order_by('vehicle')
    context={"header": "All vehicles", "message": a}
    return render(request, 'vehicles_list.html', context)
    

def vehicle(request, vehicle_id):
    a=Vehicle.objects.get(id=vehicle_id)
    b=Rental.objects.filter(vehicle=vehicle_id)
    date1=date.today()
    for i in b:
        print(i.return_date)
        if i.return_date==None:
            free='Not free'
        else:
            free="Free"
         
    context={"header": a.vehicle, "message": a, "message1":b, 'message2': free}
    return render(request, 'vehicle.html', context)

def add_customer(request):
    
    if request.method == "GET":
        customer_form = CustomerForm()
        print ("Loading")
        context = {'header': "Add the customer details:", 'form': customer_form}
        
    if request.method =="POST":
        a=request.GET
        customer_filled_form=CustomerForm(request.POST)
        if customer_filled_form.is_valid():
         
            customer_filled_form.save()
            context={'header': 'Saved'}
    return render(request, 'add_customer.html', context )
    

def add_vehicle(request):
    if request.method == "GET":
        vehicle_form = VehicleForm()
        print ("Loading")
        context = {'header': "Add the vehicle details:", 'form': vehicle_form}
 
    if request.method =="POST":
        b=request.GET
        vehicle_filled_form=VehicleForm(request.POST)
        if vehicle_filled_form.is_valid():
            vehicle_filled_form.save()

        context={'header': 'Saved'}

    return render(request, 'add_customer.html', context )

def add_rental(request):
    if request.method == "GET":
        rental_form = RentalForm()
        print ("Loading")
        context = {'header': "Add a rental details:", 'form': rental_form}
 
    if request.method =="POST":
        b=request.GET
        rental_filled_form=RentalForm(request.POST)
        if  rental_filled_form.is_valid():
             rental_filled_form.save()

        context={'header': 'Saved'}

    return render(request, 'add_rental.html', context )