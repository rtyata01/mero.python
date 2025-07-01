from collections import Counter, defaultdict

def shortest_substring(sentence, words):
    sentence_words = sentence.split()
    required = Counter(words)
    left = 0
    min_len = float('inf')
    result = ""
    found = defaultdict(int)
    formed = 0

    for right, word in enumerate(sentence_words):
        if word in required:
            found[word] += 1
            if found[word] == required[word]:
                formed += 1

        while formed == len(required):
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
                result = " ".join(sentence_words[left:right+1])

            left_word = sentence_words[left]
            if left_word in required:
                found[left_word] -= 1
                if found[left_word] < required[left_word]:
                    formed -= 1
            left += 1

    return result

sentence = "is one ok you the frog ok one the you is not frog"
words = ["is", "you", "frog"]
print(shortest_substring(sentence, words))