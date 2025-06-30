def is_palindrome(sub: str) -> bool:
    return sub == sub[::-1]

def find_longest_palindrome_brute_force(s: str) -> str:
    longest = ""
    n = len(s)
    
    # Generate all substrings
    for i in range(n):
        #print("->")
        for j in range(i + 1, n + 1):
            new_string = s[i:j]  # substring start with i, end with j - 1, excluding j.
            #print(new_string, end="->")
            if is_palindrome(new_string) and len(new_string) > len(longest):
                longest = new_string
    
    return longest

input = "aba"
print(f"Input: {input}, Longest Palindrome: {find_longest_palindrome_brute_force(input)}")
input = "ilikeracecar"
print(f"Input: {input}, Longest Palindrome: {find_longest_palindrome_brute_force(input)}")
input = "hellomadam"
print(f"Input: {input}, Longest Palindrome: {find_longest_palindrome_brute_force(input)}")

# Time complexity = O(n^3) = inner and outer loop o(n^2) * o(n) palindrome check