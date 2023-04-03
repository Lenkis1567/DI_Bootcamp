import random

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

a = Siamese("A", 10)
b = Chartreux("B", 2)
c = Bengal("C", 5)

all_cats=[a, b, c]
print(all_cats)

sara_pets = Pets(all_cats)
sara_pets.walk()

# =======================Dog======================
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark (self):
        print(f'The {self.name} is barking')
    def run_speed (self):
        speed = self.weight/self.age*10
        return speed
    def fight(self, another_dog):
        if (self.run_speed()*self.weight) >= (another_dog.run_speed()*another_dog.weight):
            print(f'{self.name} won')
        else:
            print (f'{another_dog.name} won')
    def play(self, dogs):
            print(f'{self.name}, {dogs} all play together.')
    def do_a_trick(self):
        if self.trained==True:
            dog_functions = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'dog_name plays dead']
            random_dog = (random.choice(dog_functions))
            print(f'{self.name} {random_dog}!')
class PetDog(Dog):
    def __init__(self, name ,age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.bark()
        self.trained = True

a = Dog("Rex", 10, 35)
b = Dog("Dolly", 3, 5)
c = Dog("Tarzan", 5, 50)
d = PetDog("Shelly", 3, 23)
a.bark()
print(c.run_speed())
b.fight(c)
dogs = ' '+b.name+', '+c.name+", "+d.name
a.play(dogs)
d.train()
d.do_a_trick()
