class ICalculator:
    def GiveMeTotal(self, first, second):
        raise NotImplementedError()
    
    def GiveMeMultiple(self, first, second):
        raise NotImplementedError()
    
    def GiveMeDifference(self, first, second):
        raise NotImplementedError()
    
class MyCalculator(ICalculator):

    def GiveMeTotal(self, first, second):
        return first + second
    
    def GiveMeMultiple(self, first, second):
        return first * second
    
    def GiveMeDifference(self, first, second):
        return first - second
    

# Testing
myCalc = MyCalculator()
first = 2
second = 3
totalValue = myCalc.GiveMeTotal(first, second)
print("Total value:", totalValue)

diffValue = myCalc.GiveMeDifference(first, second)
print("Difference value:", diffValue)

multipleValue = myCalc.GiveMeMultiple(first, second)
print("multiple value:", multipleValue)