def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    
    m, n = len(num1), len(num2)
    res = [0] * (m + n)  # create array with fixed size with 0 values [0, 0, 0, 0, 0]
    
    # Multiply from back to front
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            
            # Add mul to the position
            total = mul + res[p2]
            res[p2] = total % 10
            res[p1] += total // 10
    
    # Remove leading zeros
    result = []
    for digit in res:
        if not result and digit == 0:
            continue
        result.append(str(digit))
    
    return ''.join(result) if result else "0"


num1 = "123"
num2 = "45"
print(f"multiply {num1} * {num2} = ", multiply(num1, num2))

#      123
#   ×   45
#  ________
#      615   (123 × 5) ← shift 0 places (unit digit)
#+    4920   (123 × 4) ← shift 1 place (tens digit)
#  ________
#     5535
#


# 1st Outer loop: i = 2 (num1[2] = '3')
# Inner loop: j = 1 (num2[1] = '5')
# Multiply: 3 × 5 = 15
# Positions to update: p1 = 2 + 1 = 3, p2 = 2 + 1 + 1 = 4
# Add to res[4]: res[4] = 0 + 15 = 15
# Set res[4] = 15 % 10 = 5
# Carry to res[3] += 15 // 10 = 1

# res = [0, 0, 0, 1, 5] i = 2, j = 1
# res = [0, 0, 1, 3, 5] i = 2, j = 0

# res = [0, 0, 2, 3, 5] i = 1, j = 1,
# res = [0, 1, 0, 3, 5] i = 1, j = 0

# res = [0, 1, 5, 3, 5] i = 0, j = 1
# res = [0, 5, 5, 3, 5] i = 0, j = 0