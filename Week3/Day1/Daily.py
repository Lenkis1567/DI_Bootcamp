class Farm:
    plural_exept = {"sheep":"sheep"}
    def __init__ (self, farm_name):
        self.name = farm_name
        self.animals = {}
                        
    def add_animal (self, new_animal, quantity=1):
        if new_animal not in self.animals:
            self.animals[new_animal] = quantity
        else:
            self.animals[new_animal] += quantity 
    def get_info (self):
        print (f"{self.name}'s farm")
    def get_animal_types(self):
        return list(self.animals.keys())
    def get_short_info(self):
        # animal_str = ", ".join(list(map(lambda n: self.plural_exept.get(n, f"{n}s"), self.get_animal_types()))) - the same
        animal_str = ", ".join([self.plural_exept.get(n, f"{n}s") for n in self.get_animal_types()])

        print(f"{self.name}'s farm has  {animal_str}.")

d = Farm ("MC")
d.add_animal("cow", 5)
d.add_animal("sheep")
d.add_animal("sheep")
d.add_animal("goat", 12)
print(d.animals)
d.get_info()
print(d.get_animal_types())
d.get_short_info()

