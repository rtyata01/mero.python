gender_type = {'John':'Male', 'Carol':'Female', 'Sarah':'Female', 'Deer':'Female'}
print(gender_type)

maleCount = 0
femaleCount = 0
for key, value in gender_type.items():
    if value.lower() == 'male':
        maleCount = maleCount + 1
    elif value.lower() == 'female':
        femaleCount = femaleCount + 1
    else:
        print('Found Unknown Gender:', value)

print('Male count:', maleCount)
print('Female count:', femaleCount)

print(gender_type.keys())
print(gender_type.values())

keyList = list(gender_type.keys())
print(keyList)