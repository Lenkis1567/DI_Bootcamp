from math import pi
import turtle

class Circle:
    def __init__(self, radius:float) ->None:
        self.radius = radius
        self.diameter= radius*2

    # def __init__(self, size: float, type_of_size: 'radius') ->None:
    #     if type_of_size == 'radius':
    #         self.radius = size
    #         self.diameter = radius*2
    #     elif type_of_size =="diameter":
    #         self.radius = size/2
    #         self.diameter = diameter
    
       

    @classmethod
    def from_diameter(cls, diameter:float):
        new_circle = cls(diameter/2)
        return new_circle
    
    @property
    def area(self):
        area = pi*self.radius**2
        return area
    
    def __add__(self, other_circle):
        radius_combined = self.radius + other_circle.radius
        new_circle = Circle(radius_combined)
        return new_circle
    
    def __lt__(self, other_circle):
            return self.radius > other_circle.radius
    
    def __gt__(self, other_circle):
        return self.radius < other_circle.radius
    
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __repr__(self) -> str: #for cases with large data
        return f'(Radius: {self.radius}, Diameter: {self.diameter})'
    
        
c1 = Circle(2.0)
c2 = Circle.from_diameter(6.0)
print(c1.radius)
print(c1.diameter)

print(c2.radius)
print(c2.diameter)
c3=c1+c2
print("c3.area", c3)

circles = [c1,c3,c2]
circles.sort()
print(circles)
turtle.circle(c3.radius**3)
turtle.circle(c2.radius**2)

t=turtle.Turtle()
t.circle(c3.radius**3)