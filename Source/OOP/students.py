class Student:
    def __init__(self, name, address):
        if not name or not address:
            raise ValueError("name and address must be provided")
        self.name = name
        self.address = address
        
    def charm_symbol(self):
        match self.name:
            case "Alice":
                return f" ☀ \u2600 {self.name}"
            case "Bob":
                return f" ☁ \u2601 {self.name}"
            case "Charlie":
                return f" ☂ \u2602 {self.name}"
            case _:
                return f" ☃ \u2603 {self.name}"
    
    def __str__(self):
        return f"{self.charm_symbol()} is from {self.address}"

def main():
    print("Dictionary:")
    print_student_dictionary()
    print("Objects:")
    print_student_objects()

def print_student_dictionary():
    students = [
        {"name": "Alice", "address": "123 Maple St"},
        {"name": "Bob", "address": "456 Oak Ave"},
        {"name": "Charlie", "address": "789 Pine Rd"}
    ]
        # Print the mock students
    for student in students:
        print(f"{student['name']} is from {student['address']}")

        
def print_student_objects():
    students = [
        Student("Alice", "123 Mapler St"),
        Student("Bob", "456 Oak Ave"),
        Student("Charlie", "789 Pine Rd"),
        Student("Darwin", "123 Pine Rd"),
    ]
        # Print the mock students
    for student in students:
        print(student.charm_symbol(), student)

if __name__ == "__main__":  # It executes this main block, when running the script directly but not when importing.
    main()
