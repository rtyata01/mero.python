# The classic Gray code sequence for n bits can be constructed recursively:
# For n = 1, the Gray code sequence is [0, 1].
# For n > 1:
# Take the (n-1)-bit Gray code sequence.
# Append a reversed copy of it, but with the leading bit set to 1.


def bit_gray_code(n: int) -> list[int]:
    if n == 0:
        return [0]
    
    result = [0, 1]  # base for n=1
    for i in range(2, n + 1):
        # Prefix the existing codes with 0 for the first half
        # Then prefix reversed codes with 1 for the second half
        prefix = 1 << (i - 1)
        result += [prefix + x for x in reversed(result)]
    return result

def grayCode(n: int) -> list[int]:
    if n == 0:
        return [0]
    
    result = ["0", "1"]
    for i in range(2, n + 1):
        # Prefix '0' to the current list
        first_half = ["0" + code for code in result]
        # Prefix '1' to the reversed current list
        second_half = ["1" + code for code in reversed(result)]
        result = first_half + second_half
    
    # Convert binary strings to integers
    return [int(code, 2) for code in result]

print(f"Expected: 4, Computed:", bit_gray_code(2)) # 00, 01, 11, 10
print(f"Expected: 14, Computed:", bit_gray_code(4)) # 0000, 0001, 0010, 0011, 0101, 0110, 0111, 1000, 1001, 1010, 1100, 1101, 1110, 1111

print(f"Expected: 4, Computed:", grayCode(2)) # 00, 01, 11, 10
print(f"Expected: 14, Computed:", grayCode(4))