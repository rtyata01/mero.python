def candy_same_ratings_get_same(ratings):
    unique_sorted = sorted(set(ratings))  # Unique ratings in sorted order
    rating_to_candies = {rating: i + 1 for i, rating in enumerate(unique_sorted)}  # Map rating → candy count

    candies = [rating_to_candies[r] for r in ratings]
    return sum(candies)

ratings = [1, 2, 2]
print(candy_same_ratings_get_same(ratings))  # Output: 5

ratings = [1, 2, 2, 3, 2]
print(candy_same_ratings_get_same(ratings))  # Output: 10