class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        print("Calling getRadius method")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set the value of radius, if negative raise error"""
        print("Calling setRadius method")
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must of postive")
        
    @property
    def area(self):
        """Calculate the area of circle"""
        return self.pi() * self.radius**2
    
    def cylinder_volume(self, height):
        """Calculate the volume of cylinder with circle as base"""
        return self.area * height
    
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)
    
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
    
c = Circle(5)
print(c.radius)

print(c.area)

c.radius = 2
print(c.area)

print("cylinder_volume =>", c.cylinder_volume(height=4))

c = Circle.unit_circle()
print(c.radius)

print(c.pi())
print(Circle.pi())

c.radius = -1
c.area = 100