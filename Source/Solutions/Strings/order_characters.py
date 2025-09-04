from collections import Counter, defaultdict

def custom_sort(input_str, order):
    # count = {}                      
    # for char in input_str:
    #    count[char] = count.get(char, 0) + 1
        
    count = defaultdict(int)  # preserver order of insertion, {'b': 2, 'a': 1, 'c': 3}
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
    count = Counter(input_str)  # does not preserve the order, Counter({'a': 3, 'n': 2, 'b': 1})
    result = []

    # Add characters in the specified order
    for ch in order:
        result.append(ch * count.pop(ch, 0)) # if ch is not present, then it results 0, which refers it appends empty string ch * 0.

    # Append the remaining characters in any order (relative order not preserved in counter)
    for ch, freq in count.items():
        result.append(ch * freq)

    return ''.join(result)


# Example usage
test_cases = [
    ("bbabac","abc"),
    ("dbbaebacf","abc"),
]

for test_case in test_cases:
    input_str, order_str = test_case
    print(f"Expected order: {order_str},  input: {input_str}, output: {custom_sort_relative_order(input_str, order_str)}") 
    print(f"Expected order: {order_str},  input: {input_str}, output: {custom_sort(input_str, order_str)}") 
