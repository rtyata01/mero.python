def find_max_balanced_parentheses(s):
    open_brace_count = 0
    cur_length = 0
    cur_start = 0
    max_start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            open_brace_count += 1
        elif char == ')' and open_brace_count > 0:
                open_brace_count -= 1
                cur_length += 2
                if cur_length > max_length:
                    max_length = cur_length
                    max_start = i - max_length + 1
                    #print(f"Start Index: {max_length_start_index}, Max Length: {max_length}")
                    
        if open_brace_count == 0:
            cur_start = i - max_length + 1
            cur_length = 0

    return max_length, s[max_start: max_start + max_length]

# Test the function
test_input = "(((()()))))(())"
print("Original string:", test_input)
length, substring = find_max_balanced_parentheses(test_input)
print("Result .............................")
print("Maximum Length:", length) 
print("Balanced Substring:", substring)

test_input = "(())(((()()))))"
print("Reversed Original string:", test_input)
length, substring = find_max_balanced_parentheses(test_input)
print("Result .............................")
print("Maximum Length:", length) 
print("Balanced Substring:", substring)