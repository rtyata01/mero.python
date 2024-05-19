import json

with open('d:\git\mero.python\Source\Json Parsing\studentsData.json', 'r') as jsonFile:
    data = json.load(jsonFile)

students = data['students']
unique_names = set()

for student in students:
    unique_names.add(student["name"])

print("Unique Names")
for unique_name in unique_names:
    print(unique_name)

new_student = {
    "id": 6,
    "name": "Hary",
    "age": 21,
    "grade": "B"
}

students.append(new_student)
updated_data = json.dumps(data, indent=4)

with open('d:\git\mero.python\Source\Json parsing\studentsData.json', 'w') as file:
    file.write(updated_data)