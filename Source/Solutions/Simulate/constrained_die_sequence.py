# Given: An integer n: total number of die rolls.
# A list rollMax of size 6: where rollMax[i] is the maximum number of times face i+1 can appear consecutively.
# Return the number of distinct valid sequences of dice rolls of length n that obey all the rollMax constraints.
# Result should be returned modulo 10⁹ + 7

# die = one die = has six side.
# dice = tow or more die.

MOD = 10**9 + 7

def dieSimulator(n, rollMax):
    cache = {}
    
    def count_die_sequences(i, last_face, streak):
        key = (i, last_face, streak)
        if key in cache:
            return cache[key]
        
        if i == 0:
            return 1  # successfully formed a valid sequence

        total = 0
        for face in range(6):
            if rollMax[face] == 0:
                continue
            if face == last_face:
                if streak < rollMax[face]:
                    total += count_die_sequences(i - 1, face, streak + 1)
            else:
                total += count_die_sequences(i - 1, face, 1)

        cache[(i, last_face, streak)] = total
        return total % MOD

    # start with no last_face (-1) and 0 streak
    return count_die_sequences(n, -1, 0)

n = 3  # sequence of size 3
rollMax = [1, 2, 0, 0, 0, 0]
print(f"Expected: 4, Output: ", dieSimulator(n, rollMax))
# Allowed = [1, 2, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1] = 4 sequence

n = 2
rollMax = [1, 1, 1, 2, 2, 3]
print(f"Expected: 33, Output: ", dieSimulator(n, rollMax))