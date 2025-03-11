from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name: str):
        print(f"{name} ...")
        self.name = name
        
    @abstractmethod
    def make_sound(self) -> None:
        pass
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
        

class Dog(Animal):
    def make_sound(self):
        print("woof woof")
        
        
class Cat(Animal):
    def make_sound(self):
        print("meou meou")

# Testing
if __name__ == "__main__":
    dog = Dog("Rookie")
    dog.make_sound()
    dog.sleep()
    
    cat  = Cat("Snookie")
    cat.make_sound()
    cat.sleep()
        
        