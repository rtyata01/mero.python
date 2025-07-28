# A number is strobogrammatic if it looks the same after a single 180-degree rotation.
# Rotate the number by 180,
  # Only digits that look the same after rotation alone are 0, 1, and 8 
  # 6 and 9 are not strobogrammatic numbers.
  # 6 when rotated 180, will become 9. 9 becomes 6 when rotated 180.  9 != 6.
  # 69 when rotated 180, will become 96 and 96 looks same as 69.

def is_strobogrammatic(num: str) -> bool:
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    left = 0
    right = len(num) - 1
    
    while left <= right:
        if num[left] not in mapping or num[right] not in mapping:
            return False
        if mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    
    return True


def find_strobogrammatic(n: int) -> list:
    pairs = [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]

    def build(n, final_length):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        
        prev = build(n - 2, final_length)
        result = []

        for number in prev:
            for a, b in pairs:
                # Prevent numbers from starting with 0 (unless it's the only digit)
                if n == final_length and a == '0':
                    continue
                result.append(a + number + b)
        return result
    
    return build(n, n)

# Time Complexity = 0(5^n/2), where 5 refers the pairs and n is the length.
# Space Complexity = 0(n * 5^n/2)

# Test
print(f"Expected: True, Output: ", is_strobogrammatic("69"))  # True
print(f"Expected: True, Output: ", is_strobogrammatic("88"))  # True
print(f"Expected: True, Output: ", is_strobogrammatic("6699"))  # True
print(f"Expected: False, Output: ", is_strobogrammatic("962")) # False
print(f"Expected: False, Output: ", is_strobogrammatic("01")) # False

# Test
print(find_strobogrammatic(1))  # ['11', '69', '88', '96']
print(find_strobogrammatic(2))  # ['11', '69', '88', '96']
print(find_strobogrammatic(3))  # ['101', '609', '808', '906', '111', '619', ...]
