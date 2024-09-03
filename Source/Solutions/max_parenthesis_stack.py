def find_max_balanced_parentheses(s):
    stack = []  # Stack to keep track of indices of '('
    length = 0
    start_index = -1  # Start index of the longest balanced substring
    max_length = 0  # Maximum length of balanced parentheses
    max_start_index = 0
    
    
    for i, char in enumerate(s):
        if char == '(':
            # Push the index of '(' onto the stack
            stack.append(char)
        elif char == ')' and stack:
            # Pop the last unmatched '(' index from the stack
            stack.pop()
            
            # Calculate the length of the current balanced substring
            length += 2
                
            # Update max_length and start_index if necessary
            if length > max_length:
                max_length = length
                max_start_index = i - max_length + 1
                
        if not stack:
            length = 0
            start_index = i - max_length + 1
            
    # Extract the longest balanced substring using start_index and max_length
    longest_balanced_substring = s[max_start_index:max_start_index + max_length] if start_index != -1 else ""
    
    return max_length, longest_balanced_substring

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

