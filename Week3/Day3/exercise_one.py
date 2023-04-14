
# =====Exercise 3: String module===============
import random
import string
from func import adding
print(adding(1,6))

from func import random_compare
b = input("Print a number between 1 and 100: ")
random_compare(b)

list_alph = list(string.ascii_letters)
l=''
for i in range(0,4):
    al = random.randint(0,51)
    l+=list_alph[al]
print(l)
# ============Exercise 4 : Current Date==================
from datetime import date
today = date.today()
print(today)
# ============Exercise 5 : Amount of time left until January 1st==================
from datetime import date

def till_ny():
    import datetime
    today = datetime.datetime.now()
    ny = datetime.datetime(2024,1,1,0,1)
    time_diff = ny - today
    print(f"New year is in {time_diff}")

    tdays = time_diff.days
    print(f"NY is in {tdays} days.")

till_ny()
# ===================== 6 Birthday and minutes=================
def life_days():
    import datetime
    today = datetime.datetime.now()
    birdthay_d = int(input("Input the day of your birth: "))
    birthday_m= int(input("Input the month of your birth: "))
    birthday_year = int(input("Input the year of your birth: "))
    birthday = datetime.datetime(birthday_year, birthday_m, birdthay_d ) 
    
    time_diff = today - birthday
    a=str(time_diff)
    a=a[0:19]
    print(f"You lived {a} minutes")

life_days()
# =================7 Upcoming Holiday===============================
def holiday_time():
    import datetime
    today = datetime.datetime.today()
    print(today)
    holiday=datetime.datetime(2023,4,26,0,0,0)
    time_till_holiday=holiday-today
    str=f"Till holiday {time_till_holiday}"
    print(str[0:27], "min")
holiday_time()
# =======================Exercise 8 : How Old Are You On Jupiter?================
def age_anotherplanet(age, planet):
    earth=31557600
    koeff={"earth":31557600, "mercury":earth*0.2408467,"venus": earth*0.61519726, "mars":earth*1.8808158, "jupiter": earth*11.862615,"saturn": earth*29.447498,"uranus":earth*84.016846, "neptune":earth*164.79132}
    
    return round(age/koeff[planet], 2)
age=int(input("Input your age in seconds: "))
planet=input("Input the planet you wanna live: ")
print(age_anotherplanet(age,planet))
# ======================Exercise 9 : Faker Module=========
from faker import Faker
fake = Faker()
users=[]

quantity=int(input("How many people do you need? "))
for i in range (0,quantity):
    user={}
    user["Name"]= fake.unique.name()
    user["Address"]=fake.address()
    user["Langage code"]="eng"
    users.append(user)

print(users)




