class Employee:
    def __init__(self, name, salary):
        self.name = name         # Public property
        self.salary = salary    # Proteced property or Private property (Encapsulation)
        self.__bonus = 50000     # Strongly Private property (Name Mangling)

    # Getter for salary, decorator
    @property
    def salary(self):
        return self._salary

    # Setter for salary, decorator
    @salary.setter
    def salary(self, value):
        if value < 30000:
            raise ValueError("Salary must be at least 30,000!")
        self._salary = value

    def show_details(self, is_manager = False):
        if is_manager:
            return f"Employee: {self.name}, Salary: {self._salary}, Bonus:{self.__bonus}"
        else:
            return f"Employee: {self.name}, Salary: {self._salary}"

# Creating an object
employee = Employee("Alice", 50000)

# Accessing salary using getter
print(f"Employe Details: {employee.show_details()}")  

# Updating salary using setter
employee.name = "Bob"
employee.salary = 80000
employee.__bonus = 90000  # python creates a new public property __bonus.
print(f"Employee Details: {employee.show_details()}")
print(f"Employee Bonus: {employee.__bonus}")

print(f"Employe Details: {employee.show_details(is_manager=True)}")  

