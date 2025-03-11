from abc import ABC, abstractmethod

class ICalculator(ABC):
    
    @abstractmethod
    def add(self, first: float, second: float) -> float:
        pass
    
    @abstractmethod
    def multiply(self, first: float, second: float) -> float:
        pass
    
    @abstractmethod
    def subtract(self, first: float, second: float) -> float:
        pass
    
class MyCalculator(ICalculator):

    def add(self, first: float, second: float) -> float:
        return first + second
    
    def multiply(self, first: float, second: float) -> float:
        return first * second
    
    def subtract(self, first: float, second: float) -> float:
        return first - second
    

# Testing
if __name__ == "__main__":
    my_calc = MyCalculator()
    first, second = 12, 5
    
    print("Total value:", my_calc.add(first, second))
    print("multiple value:", my_calc.multiply(first, second))
    print("Difference value:", my_calc.subtract(first, second))
