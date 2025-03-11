import os
import csv
from collections import namedtuple

# Get the script's directory
script_dir = os.path.dirname(__file__)  

# Construct the full path to names.txt
file_path = os.path.join(script_dir, "names.csv")

Student = namedtuple('Student', ['name', 'gender', 'age'])

def create_student(row: str) -> Student:
    name, gender, age = (row + ["", "", ""])[:3]  # Ensure 3 elements, fill missing with ""
    return Student(name.strip(), gender.strip(), age.strip())

students = []
with open(file_path, "r") as file:
    for line in file:  
        row = line.strip().split(",")
        new_student = create_student(row)
        students.append(new_student)

for student in students:
        print(student.name, student.gender, student.age, sep=", ")
      
print()        
students = []
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        new_student = create_student(row)
        students.append(new_student)

for student in students:
        print(student.name, student.gender, student.age, sep=", ")