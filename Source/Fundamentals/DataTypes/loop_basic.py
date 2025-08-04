    
i = 5
while i != 0:
    print(f"Run {i}")
    i = i - 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stop_index = 10
print("\nEven numbers below:", stop_index)
for num in numbers:
    if num == 8:
        print("Skipping 8")
    elif num % 2 == 0:
        print(num)
    elif num >= stop_index: # stop the loop, when it the stop index
        break

print("\nArrays")

for i in range(1, 4):  #columns
    for j in range(1, 7):  #rows
        print(i * j, end="\t") # Add tab separation.
    print() # Move to next line.
    
