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
            res.append("".join(path))
            return
        
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()  # backtrack

    backtrack(0, [])
    return res

print(letterCombinations("3"))
# Output: ['d', 'e', 'f']     

print(letterCombinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

