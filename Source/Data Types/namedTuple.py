newPerson = ('John', 10, 'male', 234567890)
print(newPerson)

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'gender', 'phone'])
person = Person(name="John", age=20, gender='malse', phone=234567890)
print(person.name, person.age, person.gender, person.phone)