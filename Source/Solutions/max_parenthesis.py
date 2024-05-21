def find_max_balanced_parenthesis(s):
    open_count = 0
    result =''

    for char in s:
        if char == '(':
            open_count += 1
            result += char
        elif char == ')' and open_count > 0:
            open_count -= 1
            result += char

    # remove any remaining parenthesis left
    result = result[:len(result) - open_count]
    return result

# Test the function
s = "((())()()))))(())"
print("Original string:", s)
print("Max balanced string:", find_max_balanced_parenthesis(s))