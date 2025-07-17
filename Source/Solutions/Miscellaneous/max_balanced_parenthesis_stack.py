# Hard: Given a string containing '(' and ')', find the length of the longest valid parentheses substring.

# this will treat, consecutive balanced as one balanced string i.e. (())(((()()))) i.e. 4 + 10 = 14.
def find_max_balanced_parentheses_substring(s):
    stack = [-1]  # Initial index for base calculation
    max_length = 0
    start_index = 0  # Start index of the longest valid substring

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')' and stack:
            stack.pop()
            if stack:
                length = i - stack[-1]
                if length > max_length:
                    max_length = length
                    start_index = stack[-1] + 1
            else:
                stack.append(i)  # Reset base index
    longest_balanced_substring = s[start_index:start_index + max_length]
    return max_length, longest_balanced_substring

# Test the function
test_input = "(((()()))))(())"
print("Original string:", test_input)
length, substring = find_max_balanced_parentheses_substring(test_input)
print("Result .............................")
print("Maximum Length:", length) 
print("Balanced Substring:", substring)

test_input = "(())(((()()))))"
print("Original string:", test_input)
length, substring = find_max_balanced_parentheses_substring(test_input)
print("Result .............................")
print("Maximum Length:", length) 
print("Balanced Substring:", substring)

