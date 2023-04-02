# ======CATS===========
class Cat:
    info = []
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        Cat.info.append(self)

c = Cat("Cian", 10)
d = Cat("Dean", 1)
name, age = input("name, age separated by comma:").split(",")
age_int = int(age)
b = Cat(name, age_int)
biggest = Cat.info[0]
for cat in Cat.info:
    if cat.age >biggest.age:
        biggest = cat
print(biggest.name, ",", biggest.age)
======DOGS===========
class Dog:
    def __init__ (self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    def bark (self):
        print(self.name + " goes Woof.")
    def jump (self):
        print(f'{self.name} jumps {self.height*2} cm heigh.')
d = Dog("Dean", 20)
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(davids_dog.name, ",", davids_dog.height)
davids_dog.bark()
davids_dog.jump()
print(sarahs_dog.name, ",", sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()
if sarahs_dog.height < davids_dog.height:
    print ("The highest dog is ", davids_dog.name)

# =================Who’s the song producer==========
class Song:
    def __init__ (self, song_lyrics: list[str]):
        self.lyrics = song_lyrics
    def sing_me_a_song(self):
        for string in self.lyrics:
            print(string)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
# ============Afternoon at the Zoo=============

class Zoo:
    def __init__ (self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.sorted_animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal) 
    def get_animals(self):
        print("Here are the animals: ",self.animals)
    def sell_animal (self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.sorted_animals=sorted(self.animals)
    def alphabet_animals(self):
        self.sort_animals()
        count=0
        last_letter = None
        result = dict()
        for animal in self.sorted_animals:
            letter=animal[0]
            if letter==last_letter:
                if isinstance(result[count], str):
                    result[count] = [result[count], animal]
                else:
                    result[count].append(animal)  
            else:
                count+=1
                result[count] = animal
                last_letter=letter
        return result
    def get_groups(self):
        zoo = self.alphabet_animals()
        for animals in zoo:
            print(f"{animals}: {zoo[animals]}")

        
r = Zoo("Ramat Gan Safari")        

r.add_animal("Ape")
r.add_animal("Baboon")
r.add_animal("Bear")
r.add_animal("Emu")
r.add_animal("Eel")
r.add_animal("Elefant")
r.add_animal("Monkey")
r.get_animals()


animal_sold = input ("input a sold animal: ")
r.sell_animal(animal_sold)
r.get_animals()
r.sort_animals()
print(r.alphabet_animals())
r.get_groups()