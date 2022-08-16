import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return math.sqrt((self.coor2[1] - self.coor1[1])**2 + (self.coor2[0] - self.coor1[0])**2)
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

import cmath
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*cmath.pi*self.radius**2
    
    def surface_area(self):
        return 2*cmath.pi*self.radius**2 + 2*cmath.pi*self.radius*self.height

# EXAMPLE OUTPUT
c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())