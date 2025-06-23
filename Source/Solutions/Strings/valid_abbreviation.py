# check if a given string (like "u12uz4n") is a valid abbreviation of a word (like "internationalization"), based on a common abbreviation format.
def valid_abbreviation(word, abbr):
    i = j = 0
    word_len, abbr_len = len(word), len(abbr)
    
    while i < word_len and j < abbr_len:
        if abbr[j].isdigit():
            if abbr[j] == '0':
                return False
            num = 0
            while j < abbr_len and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if i >= word_len or word[i] != abbr[j]:
                return False
            i +=1
            j +=1
    
    return i == word_len and j == abbr_len
print(f"Expected: True, Result: ", valid_abbreviation("", ""))

print(f"\nExpected: True, Result: ", valid_abbreviation("internationalization", "i18n"))
print(f"Expected: True, Result: ", valid_abbreviation("internationalization", "20"))
print(f"Expected: False, Result: ", valid_abbreviation("internationalization", "u12uz4n"))
print(f"Expected: False, Result: ", valid_abbreviation("internationalization", "i018n"))

print(f"\nExpected: False, Result: ", valid_abbreviation("apple", "a2e"))
print(f"Expected: True, Result: ", valid_abbreviation("apple", "a3e"))
print(f"Expected: True, Result: ", valid_abbreviation("apple", "5"))
print(f"Expected: False, Result: ", valid_abbreviation("apple", "05"))
