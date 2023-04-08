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

# ==============================
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
# ===================== Birthday and minutes=================
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
# =================Upcoming Holiday===============================
# ====================================================================
