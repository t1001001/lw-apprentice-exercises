from abc import ABC, abstractmethod
from math import pi

# Geometry interface
class Geometry(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perim(self) -> float:
        pass

# Rectangle class
class Rectangle(Geometry):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perim(self) -> float:
        return 2 * (self._width + self._height)

# Circle class
class Circle(Geometry):
    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius * self._radius

    def perim(self) -> float:
        return 2 * pi * self._radius
    
# Function to measure both area and perimeter
def measure(g: Geometry):
    print(g)
    print(g.area())
    print(g.perim())

# Instantiate classes
rect = Rectangle(
    width = 3,
    height = 4
)

circle = Circle(
    radius = 5
)

measure(rect)
measure(circle)