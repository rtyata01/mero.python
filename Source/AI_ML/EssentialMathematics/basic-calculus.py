from sympy import symbols, diff, integrate

# Define the variable
x = symbols('x')

# Define the function
f = x**3 + 2*x**2 - 5*x + 1

f_prime = diff(f, x)  # derivative of f with respect to x, slope function of f(x).
print(f"The derivative f'(x) = {f_prime}")

f_integral = integrate(f, x)  # indefinite integral ∫f(x)dx
print(f"The indefinite integral ∫f(x)dx = {f_integral} + C")

f_definite_integral = integrate(f, (x, 0, 2))  # ∫f(x)dx from 0 to 2
print(f"The definite integral of f(x) from 0 to 2 = {f_definite_integral}")