nameGender = {'John':'Male', 'Carol':'Female', 'Sarah':'Female', 'Deer':'Animal'}
print(nameGender)

maleCount = 0
femaleCount = 0
for key, value in nameGender.items():
    if value.lower() == 'male':
        maleCount = maleCount + 1
    elif value.lower() == 'female':
        femaleCount = femaleCount + 1
    else:
        print('Found Unknown Gender:', value)

print('Male count:', maleCount)
print('Female count:', femaleCount)

print(nameGender.keys())
print(nameGender.values())

keyList = list(nameGender.keys())
print(keyList)