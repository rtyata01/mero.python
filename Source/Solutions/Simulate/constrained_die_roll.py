# Roll die, with constraint rollMax. 
# It allows specific dic face to roll consecutively i.e. repeatedly as specified by rollMax array.

# die = one die = has six side.
# dice = tow or more die.

import random

def constrained_die_roll(n, rollMax):
    results = []
    last_face = None
    current_streak = 0

    for _ in range(n):
        allowed_faces = []
        for face in range(1, 7):
            if rollMax[face - 1] == 0:
                continue  # this face is not allowed at all

            if face == last_face and current_streak < rollMax[face - 1]:
                    allowed_faces.append(face)
            else:
                allowed_faces.append(face)

        if not allowed_faces:
            raise ValueError("No valid dice face can be rolled due to constraints.")

        roll = random.choice(allowed_faces)
        results.append(roll)

        if roll == last_face:
            current_streak += 1
        else:
            last_face = roll
            current_streak = 1

    return results

# Example usage
n = 10
rollMax = [2, 0, 1, 2, 2, 3]
result = constrained_die_roll(n, rollMax)
print("Constrained Die Roll:", result)

# rollMax[0] = 2 means, face 1 cannot appear more than 2 time consecutively. if it appears 3rd time consecutively, then it should be blocked.
# rollMaz[1] = 0 means, face 2 cannot appear at all. If it appears face 2, then roll again for different face.
# But it can appear multiple times in total — just not back-to-back consecutively.

# Example usage
# rollMax = [1, 0, 0, 0, 0, 0] # in this case only n=1 is possible i.e. [1], any higher value of n will result constraint failure.