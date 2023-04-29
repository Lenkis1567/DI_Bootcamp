import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise.settings')
django.setup()

from rent.models import Customer, Vehicle_type, Vehicle_size, Vehicle, Rental_Rate, Rental
from faker import Faker
import random 
from datetime import date, datetime


fake=Faker()
# for i in range(1,50):
#     if __name__ == '__main__':

#         print("Populating database")
    
#         new_customer = Customer(first_name=fake.first_name(),
#                   last_name=fake.last_name(),
#                   email=fake.email(),
#                   phone_number=fake.phone_number(),
#                   address=fake.address(),
#                   city=fake.city(),
#                   country='Israel')
#         new_customer.save()

list_size=Vehicle_size.objects.all()
list_customers=Customer.objects.all()
rentals = Rental.objects.all()



# for i in range(1,50):
#     if __name__ == '__main__':
#         new_vehicle=Vehicle(vehicle=random.choice(list_vehicle),
#                             date_created=fake.date(),
#                             real_cost=random.randint(5000, 30000),
#                             size=random.choice(list_size),
#                             )
#         new_vehicle.save()

# list_vehicle=Vehicle.objects.all()

# if __name__ == '__main__':
#     print("Populating database")
#     while len(rentals) < 100:
#         start_date=date(2010,1,1)
#         rental_date=fake.date_between(start_date, datetime.now())
#         return_date=fake.date_between(start_date, datetime.now())
#         if return_date<rental_date:
#             continue

#         def _check_rental(rental: Rental) -> bool:
#             if rental_date > rental.rental_date:
#                 if rental.return_date == None or rental.return_date >= rental_date :
#                     return True
#             elif return_date >= rental.rental_date and return_date < rental.return_date:
#                 return True
            
#             return False
                
#         active_rentals = list(filter(lambda r: _check_rental(r), rentals))
#         availble_customers = list(filter(lambda c: all(ar.customer.id != c.id for ar in active_rentals), list_customers))
#         availble_vehicle = list(filter(lambda v: all(ar.vehicle.id != v.id for ar in active_rentals) and v.date_created < rental_date, list_vehicle))

#         new_rental=Rental(            
#             customer=random.choice(availble_customers),
#             vehicle=random.choice(availble_vehicle),
#             rental_date=rental_date,
#             return_date=return_date
#         )
#         new_rental.save()
#         rentals = Rental.objects.all()
