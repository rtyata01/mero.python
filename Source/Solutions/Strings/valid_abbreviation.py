# check if a given string (like "u12uz4n") is a valid abbreviation of a word (like "internationalization"), based on a common abbreviation format.
def valid_abbreviation(word, abbr):
    w_index = a_index = 0
    
    while w_index < len(word) and a_index < len(abbr):
        if abbr[a_index].isdigit():
            if abbr[a_index] == '0':
                return False
            num = 0
            while a_index < len(abbr) and abbr[a_index].isdigit():
                num = num * 10 + int(abbr[a_index])
                a_index += 1
            w_index += num
        else:
            if w_index >= len(word) or word[w_index] != abbr[a_index]:
                return False
            w_index +=1
            a_index +=1
    
    return w_index == len(word) and a_index == len(abbr)

print(f"Expected: True, Result: ", valid_abbreviation("", ""))
print(f"\nExpected: True, Result: ", valid_abbreviation("internationalization", "i18n"))
print(f"Expected: True, Result: ", valid_abbreviation("internationalization", "20"))
print(f"Expected: False, Result: ", valid_abbreviation("internationalization", "u12uz4n"))
print(f"Expected: False, Result: ", valid_abbreviation("internationalization", "i018n"))

print(f"\nExpected: False, Result: ", valid_abbreviation("apple", "a2e"))
print(f"Expected: True, Result: ", valid_abbreviation("apple", "a3e"))
print(f"Expected: True, Result: ", valid_abbreviation("apple", "5"))
print(f"Expected: False, Result: ", valid_abbreviation("apple", "05"))
