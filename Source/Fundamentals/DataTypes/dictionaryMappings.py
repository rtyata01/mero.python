name_gender_mappings = {
    "John": "Male", 
    "Carol": "Female", 
    "Sarah": "Female", 
    "Deer": "Female"
    }

print(name_gender_mappings)

maleCount = 0
femaleCount = 0
for key, value in name_gender_mappings.items():
    if value.lower() == 'male':
        maleCount = maleCount + 1
    elif value.lower() == 'female':
        femaleCount = femaleCount + 1
    else:
        print('Found Unknown Gender:', value)

print("Male count:", maleCount)
print("Female count:", femaleCount)
print("Carol is a", name_gender_mappings["Carol"])

print(name_gender_mappings.keys())
print(name_gender_mappings.values())

for name in name_gender_mappings:
    print(name, name_gender_mappings[name], sep=", ")
