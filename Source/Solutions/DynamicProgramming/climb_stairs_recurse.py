# Medium: Counting Ways to Climb Stairs
# Given n number of stairs, find how many different ways to climb to the top, if one can climb 1 or 2 steps at a time.

def find_ways_to_climb(stairs, path=None, result=None):
    if path is None:
        path = []
    if result is None:
        result = []

    # Base case: reached exactly the top
    if stairs == 0:
        result.append(path)
        return

    # Take a 1-step if possible
    if stairs >= 1:
        find_ways_to_climb(stairs - 1, path + [1], result)

    # Take a 2-step if possible
    if stairs >= 2:
        find_ways_to_climb(stairs - 2, path + [2], result)

    return result

def print_ways_to_climb(stairs):
    ways = find_ways_to_climb(stairs)
    print(f"Number of ways to climb: {len(ways)} with stairs count: {stairs}")
    print("Ways to climb the stairs:")
    for i, way in enumerate(ways, 1):
        print(f"{i}: {way}")
    return len(ways)

# Example usage
print_ways_to_climb(stairs=3)
print_ways_to_climb(stairs=5)
