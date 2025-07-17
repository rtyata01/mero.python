def find_unique_palindromes(source, fixedLength):
    n = len(source)
    
    if n < fixedLength:
        return []
    
    def collect_palindromes(left, right):
        while left >= 0 and right < len(source) and source[left] == source[right]:
            if right - left + 1 >= fixedLength:
                result.add(source[left:right + 1])
            left -= 1
            right += 1
        return source[left + 1: right]
    
    result = set()
    for i in range(len(source)):
        # Odd-length palindromes
        collect_palindromes(i, i)
        # Even-length palindromes
        collect_palindromes(i, i + 1)
            
    return list(result)

result = find_unique_palindromes("abcba", 3)
print(f"Unique palindrome count: {len(result)}, palindromes: {result}")
longest = max(result, key=len) if result else None
print(f"Longest palindrome: {longest}")

result = find_unique_palindromes("ilikeracecar", 3)
print(f"Unique palindrome count: {len(result)}, palindromes: {result}")
longest = max(result, key=len) if result else None
print(f"Longest palindrome: {longest}")