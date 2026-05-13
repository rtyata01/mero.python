# Outcomes of a die
outcomes = [1, 2, 3, 4, 5, 6]

# Probabilities for a fair die
probabilities = [1/6] * 6  # Each face has probability 1/6

# Print the probability distribution
for outcome, prob in zip(outcomes, probabilities):
    print(f"P(X = {outcome}) = {prob:.2f}")