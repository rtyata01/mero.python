class Solution:
    def find_ways_to_climb(self, n, path=None, result=None):
        if path is None:
            path = []
        if result is None:
            result = []

        # Base case: reached exactly the top
        if n == 0:
            result.append(path)
            return

        # Take a 1-step if possible
        if n >= 1:
            self.find_ways_to_climb(n - 1, path + [1], result)

        # Take a 2-step if possible
        if n >= 2:
            self.find_ways_to_climb(n - 2, path + [2], result)

        return result

    def num_stairs(self, n):
        ways = self.find_ways_to_climb(n)
        print(f"Number of ways: {len(ways)}")
        print("Ways to climb the stairs:")
        for i, way in enumerate(ways, 1):
            print(f"{i}: {way}")
        return len(ways)


# Example usage
sln = Solution()
sln.num_stairs(5)
