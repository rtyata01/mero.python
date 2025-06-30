# Given a list of words, find all pairs of unique indices such that their concatenation is a palindrome.

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    word_map = {word: i for i, word in enumerate(words)}  # {'bat': 0, 'tab': 1, 'cat': 2}
    results = set()

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix, suffix = word[:j], word[j:]

            # Case 1: If prefix is palindrome, look for reversed suffix
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix != word and reversed_suffix in word_map:
                    print(f"{reversed_suffix + word}")
                    results.add((word_map[reversed_suffix], i))

            # Case 2: If suffix is palindrome, look for reversed prefix
            if j != len(word) and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix != word and reversed_prefix in word_map:
                    print(f"{word + reversed_prefix}")
                    results.add((i, word_map[reversed_prefix]))

    return list(results)

words = ["bat", "tab", "cat"]
print(palindrome_pairs(words)) # Output: [(1, 0), (0, 1)]

# j=0: prefix "" is palindrome, reversed(suffix)="tab" → exists in word_map → pair: (1, 0) => "bat" + "tab" = "battab"
# j=0: prefix "" is palindrome, reversed(suffix)="bat" → exists → pair: (0, 1) => "tab" + "bat" => "tabbat"


words = ["lls", "s", "sssll"]
print(palindrome_pairs(words)) 

words = ["ab", "a", "ba"]
print(palindrome_pairs(words)) 