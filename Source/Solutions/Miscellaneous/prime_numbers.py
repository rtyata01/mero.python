import math

def sieve_primes(start, end):
    if end < 2 or start > end:
        return []

    sieve = [True] * (end + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime

    #upper_bound = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    for i in range(2, int(math.sqrt(end)) +1): # int(end ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end + 1, i):  # mark prime as false, if divisible by 2*2, +2=4,6,8,10..., 3*3, +3=9,12,15,18
                sieve[j] = False

    # Collect primes in the specified range
    primes_in_range = [i for i in range(start, end + 1) if sieve[i]]
    return primes_in_range
    
def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Prime Numbers: {sieve_primes(10, 100)}")

num = 19
print(f"Is [{num}] Prime Number: {is_prime_number(num)}")

