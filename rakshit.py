from geom2d.point import Point
def __add__(self, other):
    return Point(
    self.x + other.x,
    self.y + other.y
)

def __sub__(self, other):
    return Point(
    self.x- other.x,
    self.y- other.y
)

x=Point(1,3)
y=Point(2,4)
print(x.distance_to(y))
print(__add__)
print(__sub__)