# find all words in a list that are concatenations of two or more other words from the same list

# Use a set for fast lookup.
# For each word, check if it can be formed by concatenating two or more words from the list.
# Use memoization or dynamic programming to speed up checking for concatenation.

def find_all_concatenated_words(words):
    word_set = set(words)
    result = []
    memo = {}

    def is_concatenated_word(word, is_original):
        if word in memo:
            return memo[word]
        
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in word_set:
                if suffix in word_set or is_concatenated_word(suffix, False):
                    memo[word] = True
                    return True
                
        memo[word] = False
        return False

    for word in words:
        if not word:
            continue
        word_set.remove(word)  # avoid using the word itself
        if is_concatenated_word(word, True):
            result.append(word)
        word_set.add(word)

    return result

words = ["cat", "cats", "dog", "catsdog", "dogcatsdog", "rat", "ratcatdogcat"]
print(find_all_concatenated_words(words))

# "catsdog" = "cats" + "dog"
# "dogcatsdog" = "dog" + "cats" + "dog" = "dog" + "catsdog" -> from memorization.
# "ratcatdogcat" = "rat" + "cat" + "dog" + "cat"