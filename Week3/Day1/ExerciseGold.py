# =============Geometry==========
class Circle:
    def __init__(self, name, radius=3.0):
        self.name = name
        self.radius = radius
    def perimetr_calc(self):
        # self.perimetr = 2*3,14*self.radius 
        return 2*3.14*self.radius
    def area_calc(self):
        # self.area = 3,14*self.radius
        return 3.14*(self.radius**2)
    def circle_def(self):
        return (f"The circle is the set of all points in the plane that are a fixed distance iqual to {self.radius} from a fixed point")

c = Circle("F")
d = Circle("D")
print(d.circle_def())
print (c)
print("length or the circle: ", c.perimetr_calc())   
print("Area of the circle:" , c.area_calc()) 
# # =============Exercise 2 Custom List Class==========
import random
class Mylist:
    def __init__(self, letters):
        self.letters=letters
    def sort(self):
        self.letters.sort()
        return self.letters
    def reversed(self):   
        self.letters.reverse()
        print(self.letters)
    def another_list(self):
        another_list=[random.randint(1,1000) for i in range(0,len(self.letters))]
        return another_list
a=Mylist(["a", "b", "c", "d", "e"])
print(a.letters)
a.reversed()
print(a.sort())
print(a.another_list())

# =======================Exercise 3 : Restaurant Menu Manager==================
class MenuManager:
    def __init__(self, name, menu):    
        self.name=name
        self.menu=menu
    def add_item(self, name, price, spice, gluten):
        new_dish={}
        new_dish['name']=name
        new_dish["price"]=price
        new_dish["spice_level"]=spice
        new_dish["gluten_index"]=gluten
        self.menu.append(new_dish)

    def remove_item(self, name):
        dishes = [i['name'] for i in self.menu]
        print(dishes)
        if name in dishes:
            self.menu.pop(dishes.index(name))
            return self.menu
        else:
            strin="There is no such dish"
            return strin

a=MenuManager("A", [{"name":"Soup", "price": "10", "spice_level": "B", "gluten_index":False}, {"name":"Hamburger", "price": "15", "spice_level": "A", "gluten_index":True}, {"name":"Salad", "price": "18", "spice_level": "A", "gluten_index":False}, {"name":"French Fries", "price": "5", "spice_level": "C", "gluten_index":False}, {"name":"Beef bourguignon", "price": "25", "spice_level": "B", "gluten_index":True}])
print(a.menu)
a.add_item("Coffee", 7, "A", False)
print(a.menu)
rem=input("Which dish to remove from menu: Soup, Salad, Coffee, French Fries? ")
print(a.remove_item(rem))