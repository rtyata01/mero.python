# Hard: Given a string containing '(' and ')', find the length of the longest valid parentheses substring.

# this will treat, consecutive balanced as one balanced string i.e. (())(((()()))) i.e. 4 + 10 = 14.
def find_max_balanced_parentheses_substring(source):
    stack = [-1]  # Initial index for base calculation
    max_length = 0
    start_index = 0  # Start index of the longest valid substring

    for i, char in enumerate(source):
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
    longest_balanced_substring = source[start_index:start_index + max_length]
    return max_length, longest_balanced_substring

# Time Complexity: O(n)
# Space Complexity: O(n)

# Test the function
test_cases = [
    "",
    ")",
    "(",
    ")(",
    "(())",
    "(((()()))))(())",
    "(())(((()()))))"
]

for input in test_cases:
    print("\nOriginal string input:", input)
    length, substring = find_max_balanced_parentheses_substring(input)
    print("Maximum Length:", length) 
    print("Balanced Substring:", substring)
    
