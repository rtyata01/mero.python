def letterCombinations(digits):
    if not digits:
        return []

    # Mapping from digit to letters
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    res = []

    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return
        
        for letter in phone_map[digits[index]]:
           backtrack(index + 1, path + letter)
           
    backtrack(0, "")
    return res

print(letterCombinations("3"))
# Output: ['d', 'e', 'f']     

print(letterCombinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

print(letterCombinations("43"))
