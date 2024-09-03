def find_longest_palindrome(s: str):
    longest = ""
    s_len = len(s)
    
    def expand_around_center(left: int, right: int):
        while left >= 0 and right < s_len and s[left] == s[right]:
            left -=1
            right +=1
        return s[left + 1: right]
        
    for i in range(s_len):
        print(f"Iterations {i}, Starting value: {s[i]}")
        # odd length palindromes (single character center)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
            print(f"Found odd palindrome: {longest}")
        
        # even length palindromes (two character center)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
            print(f"Found even palindrome: {longest}")
        
    return longest

input = "babad"
print(f"Input: {input}, Longest Palindrome: {find_longest_palindrome(input)}")
input = "ilikeracecar"
print(f"Input: {input}, Longest Palindrome: {find_longest_palindrome(input)}")
input = "hellomadam"
print(f"Input: {input}, Longest Palindrome: {find_longest_palindrome(input)}")