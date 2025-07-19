# Hard: find the Minimum Window Substring from source "sentence" and target "list of words"

from collections import Counter, defaultdict

def shortest_substring(sentence, words):
    sentence_words = sentence.split()
    required_counts = Counter(words)
    window_counts = defaultdict(int)
    
    formed = 0
    left = 0
    min_len = float('inf')
    min_window = (0, 0)

    for right, word in enumerate(sentence_words):
        if word in required_counts:
            window_counts[word] += 1
            if window_counts[word] == required_counts[word]:
                formed += 1

        while formed == len(required_counts):
            if right - left < min_len:
                min_len = right - left
                min_window = (left, right)

            left_word = sentence_words[left]
            if left_word in required_counts:
                window_counts[left_word] -= 1
                if window_counts[left_word] < required_counts[left_word]:
                    formed -= 1
            left += 1

    if min_len == float('inf'):
        return ""
    
    start, end = min_window
    return " ".join(sentence_words[start:end+1])

sentence = "this is one ok you the frog ok one the you is not frog"
words = ["is", "you", "frog"]
print(shortest_substring(sentence, words))