from django.db import models

class Vehicle_type(models.Model):
    name=models.CharField()
    def __str__(self):
        return self.name

class Vehicle_size(models.Model):
    name=models.CharField()     
    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle=models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    date_created=models.DateField()
    real_cost=models.FloatField()
    size=models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.vehicle} {self.date_created} {self.real_cost} {self.size}'

class Customer(models.Model):
    first_name=models.CharField(max_length=200, blank =False)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.CharField()
    address=models.CharField()
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number} {self.address} {self.city} {self.country}'
    
class Rental(models.Model):
    rental_date=models.DateField(blank =False)
    return_date=models.DateField(blank =False)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    def __str__(self):
       return f'{self.rental_date} {self.return_date} {self.customer} {self.vehicle}'


    
class Rental_Rate(models.Model):
    daily_rate=models.FloatField()
    vehicle_type=models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    vehicle_size=models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)

    def __str__(self):
        return self.daily_rate