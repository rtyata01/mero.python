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
            return 1, [[]]  # successfully formed a valid sequence

        total = 0
        sequences = []
        
        for face in range(6):
            if rollMax[face] == 0:
                continue
            if face == last_face:
                if streak < rollMax[face]:
                    sub_total, sub_sequences = count_die_sequences(i - 1, face, streak + 1)
                    total += sub_total
                    for seq in sub_sequences:
                        sequences.append([face + 1] + seq)
            else:
                sub_total, sub_sequences= count_die_sequences(i - 1, face, 1)
                total += sub_total
                for seq in sub_sequences:
                    sequences.append([face + 1] + seq)

        cache[key] = (total % MOD, sequences)
        return cache[key]

    # start with no last_face (-1) and 0 streak
    total_count, all_sequences = count_die_sequences(n, -1, 0)
    print("Valid sequences:")
    for seq in all_sequences:
        print(seq)
    return total_count

n = 3  # sequence of size 3
rollMax = [1, 2, 0, 0, 0, 0]
print(f"Expected: 4, Output: ", dieSimulator(n, rollMax))
# Allowed = [1, 2, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1] = 4 sequence

n = 2
rollMax = [1, 1, 0, 0, 0, 1]
print(f"Expected: 6, Output: ", dieSimulator(n, rollMax))