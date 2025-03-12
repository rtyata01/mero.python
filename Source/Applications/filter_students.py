students_dictionary = [
    {"Name": "John", "Gender": "Male"}, 
    {"Name": "Carol", "Gender": "Female"}, 
    {"Name": "Sarah", "Gender": "Female"}, 
    {"Name": "Bob", "Gender": "Male"}
]

for student in students_dictionary:
    print(student)

def is_male_gender(s):
    return s["Gender"] == "Male"

print("Selected Male Gender:")
male_students = filter(is_male_gender, students_dictionary)
for student in male_students:
    print(student)

print("Selected Male Gender:")
male_students = filter(lambda student: student["Gender"] == "Male", students_dictionary)
for student in male_students:
    print(student)
    
    
print("Selected Male Gender:")
male_students = [student for student in students_dictionary if student["Gender"] == "Male"]
for student in male_students:
    print(student)