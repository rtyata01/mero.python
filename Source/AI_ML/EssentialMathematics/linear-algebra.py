from sympy import symbols, Eq, solve

# Define variable
x = symbols('x')

# Define equation 2x + 5 = 15
equation = Eq(2*x + 5, 15)

# Solve for x
solution = solve(equation, x)
print(f"The solution is x = {solution[0]}")