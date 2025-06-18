from collections import Counter

def custom_sort(input_str, order):
    # Count characters in input string
    #count = Counter(input_str)
    
    count = {}
    for char in input_str:
        count[char] = count.get(char, 0) + 1

    # Add characters in the order specified
    result = []
    for ch in order:
        if ch in count:
            result.append(ch * count[ch])
            del count[ch]  # Remove to avoid duplication later

    # Append the remaining characters in original relative order
    for key, value in count.items():
        result.append(key * value)

    return ''.join(result)

# Example usage
input_str = "bbabac"
order = "abc"
print(f"Expected output: aabbbc", custom_sort(input_str, order)) 

# Example usage
input_str = "dbbaebacf"
order = "abc"
print(f"Expected output: aabbbcdef", custom_sort(input_str, order)) 