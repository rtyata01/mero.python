numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

stop_index = 7
print("Even numbers below:", stop_index)
for num in numbers:
    if num % 2 == 0:
        print(num)
    if num >= stop_index: # stop the loop, when it the stop index
        break

print("Arrays")

for i in range(1, 6):  #columns
    for j in range(1, 7):  #rows
        print(i * j, end="\t") # Add tab separation.
    print() # Move to next line.