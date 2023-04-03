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

c = Circle("F")
print (c)
print("length or the circle: ", c.perimetr_calc())   
print("Area of the circle:" , c.area_calc()) 
# =============Custom List Class==========