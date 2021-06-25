# Function, that tests if a number, n is a semi-prime.
def semiPrimeDetector(n):
    if n < 4: 
        return False
    factors = 0
    for i in range(2, int(n ** 0.5) + 1):
        y = n
        while y % i == 0:
            factors += 1
            if factors > 2:
                return False
            y //= i
        if y != n and y > 1: 
            factors += 1
    return factors == 2

# Function, that will print total number of semi-prime numbers below a number, n.
def semiPrimeCount(n):
    count = 0
    for i in range(4, n + 1):
        if semiPrimeDetector(i):
            count += 1
    return count

# Tests
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
semi_primes = (4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95)
non_primes = set(range(101)) - set(primes) - set(semi_primes)

print(*map(semiPrimeDetector, primes))
print(*map(semiPrimeDetector, semi_primes))
print(*map(semiPrimeDetector, non_primes))

from timeit import timeit 
from random import random

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

short_list = 7919	
wrapped = wrapper(semiPrimeDetector, short_list)
print(timeit(wrapped, number=100000))
wrapped = wrapper(semiPrimeCount, short_list)
print(timeit(wrapped, number=10))