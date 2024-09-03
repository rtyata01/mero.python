new_person = ('John', 10, 'male', 234567890)
print(new_person)

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'gender', 'phone'])
student = Person(name="John", age=20, gender='malse', phone=234567890)
print(student.name, student.age, student.gender, student.phone)