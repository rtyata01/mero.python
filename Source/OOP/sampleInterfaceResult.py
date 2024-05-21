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

    def __int__(self):
         match self.operator:
            case '+':
                return self.first + self.second
            case '-':
                return self.first - self.second
            case '*':
                return self.first * self.second
            case _:
                raise Exception("invalid operation")
    
    """
    def __int__(self):
        if self.operator == '+':
            return int(self.first + self.second)
        elif self.operator == '-':
            return int(self.first - self.second)
        elif self.operator == '*':
            return int(self.first * self.second)
        else:
            raise Exception("invalid operation")ss
    """
        

# Testing
myCalc = MyCalculator()
first = 2
second = 3
totalValue = int(myCalc.GiveMeTotal(first, second))
print("Total value:", totalValue)

diffValue = int(myCalc.GiveMeDifference(first, second))
print("Difference value:", diffValue)

multipleValue = int(myCalc.GiveMeMultiple(first, second))
print("multiple value:", multipleValue)