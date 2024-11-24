from geom2d.point import Point
from geom2d.vector import Vector

x=Point(1,3)
y=Point(2,4)
x1=Vector(1,2)
y1=Vector(3,4)
print(x.distance_to(y))
print(x.__add__(y))
print(x.__sub__(y))
print(x1.__sub__(y1))