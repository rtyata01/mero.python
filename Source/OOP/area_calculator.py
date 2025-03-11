from abc import ABC, abstractmethod
import math

class GeometricShape(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(GeometricShape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self) -> float:
        return math.pi * self.radius ** 2

class Rectange(GeometricShape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self) -> float:
        return self.width * self.height
    
class Triangle(GeometricShape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self) -> float:
        return 0.5 * self.base * self.height
    

def create_geometric_shape(shape_type: str) -> GeometricShape | None:
    shape_type = shape_type.lower()
    
    if shape_type == 'circle':
        radius = float(input("Enter the radius of the circle:"))
        shape = Circle(radius)
    elif shape_type == 'rectangle':
        width = float(input("Enter width of the rectangle: "))
        height = float(input("Enter height of the rectangle: "))
        shape = Rectange(width, height)
    elif shape_type == 'triangle':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        shape = Triangle(base, height)
    else:
        print("Unknown shape type!")
        return None
    
    return shape

def main():
    
    while True:
        shape_type = input("Enter the shape (circle, rectangle, triangle) or 'end' to stop: ").lower()
    
        if shape_type == 'end':
            print("Exiting the program")
            break
        
        shape = create_geometric_shape(shape_type)
        
        if shape:
            print(f"The area of the shape is: {shape.area()}")

if __name__ == "__main__":
    main()