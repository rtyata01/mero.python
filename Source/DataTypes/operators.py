age = 20
has_pass = True
is_vip = False

if (age >= 18 and has_pass) or is_vip:
    print("You are allowed in.")
else:
    print("Access denied.")
    
text = "hello world"
if "z" not in text:
    print("The letter 'z' is missing!")


is_raining = False
if not is_raining:
    print("Go outside!")  # Runs because `not False` is `True`
else:
    print("Stay inside.")


# (Bitwise OR)
a = 5  # 0b0101
b = 3  # 0b0011
result = a | b  # 0b0111 -> 7
print(result)  # Output: 7

# (Bitwise AND)
a = 5  # 0b0101
b = 3  # 0b0011
result = a & b  # 0b0001 -> 1
print(result)  # Output: 1

# (Bitwise XOR)
a = 5  # 0b0101
b = 3  # 0b0011
result = a ^ b  # 0b0110 -> 6
print(result)  # Output: 6

# (Bitwise NOT) - flip 0 to 1 and 1 to 0
a = 5  # 0000 0101
result = ~a  # -6 (because of two's complement representation) 
print(result)  # Output: -6 # 1111 1010
print(f"{result:08b}")  # 8-bit binary representation

#  6  =  0000 0110
#  Filp all Bits (One's complement)                 =  1111 1001
#  Negative numbers are stored in Two's complement  =  1111 0110
