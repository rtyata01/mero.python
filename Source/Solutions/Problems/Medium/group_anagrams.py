# Group strings that are anagrams of each other.

from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))  # abc, bca ->  tuple: ('a','b','c') # can also use key as ''.join(sorted(s))
        groups[key].append(word)
    return list(groups.values())

# Time Complexity: O(n * k log k) where n is the number of strings, k is the max length of a string
# sort = O(k log k)
# loop = O(n * sort)
# Space Complexity: O(n * k), each word * length of each word

# Tests
input1 = []
print("Input:", input1, "Output:", group_anagrams(input1))

input2 = [""]
print("Input:", input2, "Output:", group_anagrams(input2))

input3 = ["a"]
print("Input:", input3, "Output:", group_anagrams(input3))

input4 = ["abc", "cbd", "bac", "bca", "dcb"]
print("Input:", input4, "Output:", group_anagrams(input4))

input5 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Input:", input5, "Output:", group_anagrams(input5))