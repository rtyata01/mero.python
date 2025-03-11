class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Name must be provided!")
        self.name = name  # Public variable

    def __str__(self):
        return f"Person: {self.name}"

class SalaryAggregator:
    """Handles salary calculations for employees and managers."""

    @staticmethod
    def aggregate_salary(*employees: "Employee") -> float:
        """Calculates the total salary of given employees, including bonuses for managers."""
        total = 0
        for emp in employees:
            if not isinstance(emp, Employee):
                raise TypeError("All arguments must be instances of Employee or Manager!")
            total += emp.salary
            if isinstance(emp, Manager):  # Add bonus if it's a Manager
                total += emp.bonus
        return total

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        if not salary:
            raise ValueError("Salary must be provided!")
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()} has salary: {self.salary}"
    
    def __add__(self, other):
        return self.salary + other.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        if not bonus:
            raise ValueError("Bonus must be provided!")
        self.bonus = bonus
        
    def __str__(self):
        return f"{super().__str__()} and bonus: {self.bonus}"

def compare_employee(first, second):
    return "Same employee!" if first == second else "Different employee!"


# Test Cases
employee = Employee("Harry", 10000)
original_employee = employee  # Reference copy
print("Compare Employee:", compare_employee(employee, original_employee))
print(employee)

original_employee = Employee("Harry", 10000)  # New object with same attributes
print("Compare Employee:", compare_employee(employee, original_employee))
print(original_employee)

manager = Manager(employee.name, employee.salary, 5000)
original_employee = Employee(employee.name, employee.salary)
print("Compare Employee:", compare_employee(employee, original_employee))
print(manager)

# Compute the total salary
total_salary = employee +  original_employee + manager.salary + manager.bonus
print(f"Total Salary: {total_salary}") 

# Compute the total salary
total_salary = SalaryAggregator.aggregate_salary(employee, original_employee, manager)
print(f"Total Salary: {total_salary}") 