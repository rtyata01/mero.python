def find_nth_fibonacci(n):
    if n <= 0:
        return 0  # Handle zero or negative index
    elif n == 1:
        return 1  # Base case: 1st Fibonacci number

    f1, f2 = 0, 1  # Start from F(0) = 0, F(1) = 1
    for _ in range(2, n + 1):  # Loop from 2 to n
        f1, f2 = f2, f1 + f2
    return f2

print(f"10Th Fibonacci Number: ", find_nth_fibonacci(10))

def print_nth_fibonacci_sequence(n):
    if n <= 0:
        return [0]

    result = [0, 1]

    for i in range(2, n + 1):
        result.append(result[i - 1] + result[i - 2])

    return result

n = 10
fib_sequence = print_nth_fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n}th number: {fib_sequence}")
print(f"{n}th Fibonacci number: {fib_sequence[n]}")

def fibonacci_dp(n):
    if n < 0:
        return []

    # Base cases
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    # DP array (table)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp

# Time complexity = o (n)

n = 10
fib_sequence = fibonacci_dp(n)
print(f"Fibonacci sequence up to {n}th number: {fib_sequence}")
print(f"{n}th Fibonacci number: {fib_sequence[n]}")
