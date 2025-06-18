# Given a list of strings, 
# find the longest word such that every prefix of the word is also in the list.

def longest_word_with_prefixes(words):
    words.sort()  # o(n log n)
    valid_words = set()
    longest = ""
    
    for word in words:
        if len(word) == 1 or word[:-1] in valid_words:  # (1)            valid_words.add(word)
            if len(word) > len(longest):
                longest = word
    return longest

words = ["a", "ap", "app", "appl", "apple", "apply"]
print(longest_word_with_prefixes(words))  # Output: "apple"

# Time complexity: O(n log n), good for even million words, provided that words are not extremely long (10 - 100 characters is fine.)
# Spce complexity: 0 (n)

# If the word lenght is extremely long, then better solution would be to use Prefix Tree i.e. Trie. 
# Check the Trie solution under Trees folder.