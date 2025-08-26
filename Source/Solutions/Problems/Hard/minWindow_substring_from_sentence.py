# Hard: find the Minimum Window Substring from source "sentence" and target "list of words"

from collections import Counter, defaultdict

def shortest_substring(sentence, words):
    sentence_words = sentence.split()
    required_counts = Counter(words)
    window_counts = defaultdict(int)
    
    formed = 0
    left = 0
    min_len = float('inf')
    min_start = 0  

    for right, word in enumerate(sentence_words):
        if word in required_counts:
            window_counts[word] += 1
            if window_counts[word] == required_counts[word]:
                formed += 1

        while formed == len(required_counts):
            window_length = right - left + 1  # correct window size
            if window_length < min_len:
                min_len = window_length
                min_start = left

            left_word = sentence_words[left]
            if left_word in required_counts:
                window_counts[left_word] -= 1
                if window_counts[left_word] < required_counts[left_word]:
                    formed -= 1
            left += 1

    if min_len == float('inf'):
        return ""
    
    return " ".join(sentence_words[min_start: min_start + min_len])

sentence = "one frog ask another Aren't you okay frog you would better be okay frog"
words = ["you", "okay", "frog"]
print(shortest_substring(sentence, words))

sentence = "the quick brown fox jumps over the lazy dog"
words = ["quick", "dog"]
print(shortest_substring(sentence, words))