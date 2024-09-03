from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

class Rectange(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    

def get_shape_input():
    shape_type = input("Enter the shape (circle, rectangle, triangle): ").lower()
    
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
    shape = get_shape_input()
    
    if shape:
        print(f"The area of the shape is: {shape.area()}")

if __name__ == "__main__":
    main()