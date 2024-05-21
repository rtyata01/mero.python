class ICalculator:
    def GiveMeTotal(self, first, second):
        raise NotImplementedError()
    
    def GiveMeMultiple(self, first, second):
        raise NotImplementedError()
    
    def GiveMeDifference(self, first, second):
        raise NotImplementedError()
    
class MyCalculator(ICalculator):

    def GiveMeTotal(self, first, second):
        return Result(first, second, '+')
    
    def GiveMeMultiple(self, first, second):
        return Result(first, second, '*')
    
    def GiveMeDifference(self, first, second):
        return Result(first, second, '-')

class Result:
    def __init__(self, first, second, operator):
        self.first = first
        self.second = second
        self.operator = operator
    
    def __str__(self):
        if self.operator == '+':
            return str(self.first + self.second)
        elif self.operator == '-':
            return str(self.first - self.second)
        elif self.operator == '*':
            return str(self.first * self.second)
        else:
            raise Exception("invalid operation")
        

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