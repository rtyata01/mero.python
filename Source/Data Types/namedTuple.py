new_person = ('John', 10, 'male', 234567890)
print(new_person)
print(f'Name: {new_person[0]} and Age: {new_person[1]}')
print('Name:', new_person[0], 'and Age:', new_person[1])

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'gender', 'phone'])
student = Person(name="John", age=20, gender='malse', phone=234567890)
print(student.name, student.age, student.gender, student.phone)