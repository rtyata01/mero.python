class ICalculator:
    def give_me_total(self, first, second):
        raise NotImplementedError()
    
    def give_me_multiple(self, first, second):
        raise NotImplementedError()
    
    def give_me_difference(self, first, second):
        raise NotImplementedError()
    
class MyCalculator(ICalculator):

    def give_me_total(self, first, second):
        return first + second
    
    def give_me_multiple(self, first, second):
        return first * second
    
    def give_me_difference(self, first, second):
        return first - second
    

# Testing
myCalc = MyCalculator()
first = 2
second = 3
totalValue = myCalc.give_me_total(first, second)
print("Total value:", totalValue)

multipleValue = myCalc.give_me_multiple(first, second)
print("multiple value:", multipleValue)

diffValue = myCalc.give_me_difference(first, second)
print("Difference value:", diffValue)
