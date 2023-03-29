
import random
# --------------1------------
def display_message() -> str:
    print("I learn here")
display_message()

# -----------2-----------
def favorite_book(title:str) -> str:
    print("One of my favorite books is", title)
favorite_book("Alice")

# -----------3-----------
def describe_city(city:str, country:str) -> str:
    print(city, " is in ", country)
describe_city ("ab", "thai")

# -------------4-----------
def compare_100(num1:int) -> str|tuple:
    if num1<1 or num1>100:
        print("choose another number")
    else:
        num2 = random.randint(1, 100)
        if num1 == num2:
            print("Success")
        else:
            print("Fail", num1, num2)
compare_100(120)
# ------------------5-----------------
def make_shirt(size:int, words:str) ->str:
    print("The size of the shirt is", size, "and the text is", words)
slogan = input("make a slogan ")   
shirt_size = input("print a size ")    
make_shirt(6, slogan)

def make_shirt1() ->str:
    print("The size of the shirt is L and the text is I love Python")
make_shirt1()

# -----------------------5Bonus-------------
def make_shirt_un(**kwargs) ->str:
    print("The size of the shirt is", size, "and the text is", words)
slogan = input("make a slogan ")   
shirt_size = input("print a size ")    
make_shirt(6, slogan)

# ----------------------6--------------------
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(mags:list) -> str:
    print(mags) 
show_magicians(magician_names)
def make_great(mags:list) ->str:
    # print(f"Great {mags[0]}, Great {mags[1]}, The Great {mags[2]}")
    the_greats = ["The Great" + i for i in mags] 
    print(the_greats)
make_great(magician_names)
# -----------------------------7----------------------
def get_random_temp() ->int:
    tempr = random.randint(-10, 40)
    return tempr
print(get_random_temp())

def main() ->str:
    random_temp = get_random_temp()
    print("The temperature today is ",random_temp)
    if random_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today") 
    if 1< random_temp <= 16:
        print('Chilly! Don’t forget your coat')
    if 17 < random_temp <= 23:
        print("It's getting better")
    if 24 < random_temp <= 32:
        print("Time to swim")
    if 33 < random_temp <= 40:
        print("Stay at home")
main()
# -------------------7B---------------
def get_random_temp1(season:str) ->int:
    if season == "winter":
      tempr = random.randint(-10, 10)  
    if season == "spring":
      tempr = random.randint(8, 22)
    if season == "summer":
      tempr = random.randint(20, 45)
    if season == "autemn":
      tempr = random.randint(10, 25)
    return tempr

# a = input('Please, choose a season: winter, summer, autemn or spring ')
# print(get_random_temp1(a))
# =========================7C==========================
def get_random_temp1(season:str) ->int:
    if season == "winter":
      tempr = random.randint(-10, 10)  
    if season == "spring":
      tempr = random.randint(8, 22)
    if season == "summer":
      tempr = random.randint(20, 45)
    if season == "autemn":
      tempr = random.randint(10, 25)
    # else:
    #    print("try one more time")
    return tempr
# print(get_random_temp1(a))

def main1(season1:str) ->str:
    random_temp = get_random_temp1(c)
    print("The temperature today is ",random_temp)
    if random_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today") 
    if 1< random_temp <= 16:
        print('Chilly! Don’t forget your coat')
    if 17 < random_temp <= 23:
        print("It's getting better")
    if 24 < random_temp <= 32:
        print("Time to swim")
    if 33 < random_temp <= 40:
        print("Stay at home")
c = input('Please, choose a season: winter, summer, autemn or spring ')
main1(c)
