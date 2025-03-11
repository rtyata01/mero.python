import random

class EmployeeLocator:
    locations =  ["Gryffindor", "Hufflepouff", "Ravenclaw", "Slytherin"] 

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.locations))
        
for i in range(5):
    EmployeeLocator.sort(f"Harry{i}")