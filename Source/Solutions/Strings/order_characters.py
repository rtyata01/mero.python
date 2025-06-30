from collections import Counter, defaultdict

def custom_sort(input_str, order):
    # count = {}                      
    # for char in input_str:
    #    count[char] = count.get(char, 0) + 1
        
    count = defaultdict(int)
    for char in input_str:
        count[char] +=1

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

def custom_sort_relative_order(input_str, order):
    count = Counter(input_str)
    result = []

    # Add characters in the specified order
    for ch in order:
        result.append(ch * count.pop(ch, 0)) # if ch is not present, then it results 0, which refers it appends empty string ch * 0.

    # Append the remaining characters in any order (relative order not preserved in dict)
    for ch, freq in count.items():
        result.append(ch * freq)

    return ''.join(result)


# Example usage
input_str = "bbabac"
order = "abc"
print(f"Expected output: aabbbc", custom_sort_relative_order(input_str, order)) 

input_str = "dbbaebacf"
order = "abc"
print(f"Expected output: aabbbcdef", custom_sort_relative_order(input_str, order)) 

# Example usage
input_str = "bbabac"
order = "abc"
print(f"Expected output: aabbbc", custom_sort(input_str, order)) 

input_str = "dbbaebacf"
order = "abc"
print(f"Expected output: aabbbcdef", custom_sort(input_str, order)) 