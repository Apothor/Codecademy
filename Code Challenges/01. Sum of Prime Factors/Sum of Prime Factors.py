# Easy Difficulty
# Write a function that finds the sum of all prime factors 1.5k of a given number, n.
# Try to write your function without using trial division 1.1k!

# Using trial division
def sum_of_prime_factors(n):
    sum_of_factors = 0
    for i in range(2, n//2+1):   
        while n % i == 0: 
            sum_of_factors += i
            n /= i
    if sum_of_factors == 0:
        return "{} is a prime".format(n)
    else:
        return sum_of_factors

# Using Sieve of Eratosthenes
# TO DO
def sum_of_prime_factors(n):
    import math
    primes = (n + 1) * [1]
    factors = [];
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if j == n:
                factors.append(i)
                print('i', i)
    return (0 if len(factors) == 0 else sum(factors))    

# Intermediate Difficulty and advanced Difficulty
# Write a function that finds the sum of each unique prime factor of a given number, n. 
# For example, 3 is the only prime factor of 9.

# Using trial division
def sum_of_unique_prime_factors(n):
    sum_of_factors = 0
    unique_factors = []
    for i in range(2, n//2+1):
        while n % i == 0:
            if i not in unique_factors:
                unique_factors.append(i)
                sum_of_factors += i
            n /= i
    if sum_of_factors == 0:
        return "{} is a prime".format(n)
    else:
        return sum_of_factors

# Using Sieve of Eratosthenes
def sum_of_unique_prime_factors(n):
    primes = (n + 1) * [1]
    sum_of_factors = 0
    for i in range(2, n//2 + 1):
        if primes[i] == 1:
            for j in range(2*i, n + 1, i):
                primes[j] = 0
                if j == n:
                    sum_of_factors += i
    if sum_of_factors == 0:
        return "{} is a prime".format(n)
    else:
        return sum_of_factors