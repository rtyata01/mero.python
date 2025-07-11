# You have n children standing in a line, each with a rating ratings[i]. You want to give candies such that:
# Every child gets at least one candy.
# Any child with a higher rating than an immediate neighbor gets more candies than that neighbor.
# You want to find the minimum total number of candies you need to distribute.

def candy(ratings):
    n = len(ratings)
    candies = [1] * n  # everyone gets at least 1 candy initially

    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # Right to left pass
    for i in range(n-2, -1, -1):  # if n =3, then n-2 = 1, loop through 1, 0 and reduce by -1
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)

ratings = [1, 2, 2]
print(candy(ratings))  # Output: 4

# Left to right pass:
# i=1: ratings[1] = 2 > ratings[0] = 1 → candies[1] = candies[0] + 1 = 2 → candies = [1, 2, 1]
# i=2: ratings[2] = 2 > ratings[1] = 2? No → candies[2] stays 1
# Right to left pass:
# i=1: ratings[1] = 2 > ratings[2] = 2? No → no change
# i=0: ratings[0] = 1 > ratings[1] = 2? No → no change
# Final candies: [1, 2, 1]
# Sum = 4


ratings = [1, 2, 3]
print(candy(ratings))  # Output: 6

# Left to right:
# i=1: ratings[1] = 2 > 1 → candies[1] = candies[0] + 1 = 2 → [1, 2, 1]
# i=2: ratings[2] = 3 > 2 → candies[2] = candies[1] + 1 = 3 → [1, 2, 3]
# Right to left:
# i=1: ratings[1] = 2 > 3? No
# i=0: ratings[0] = 1 > 2? No
# Final candies: [1, 2, 3]
# Sum = 6