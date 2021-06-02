# Function to find and return the 50th number in the Fibonacci Sequence
def fibonacciFinder50():
    fib0 = 0
    fib1 = 1    
    fib_count = 2
    while fib_count < 50:
        temp = fib1
        fib1 = fib0 + fib1
        fib0 = temp
        fib_count += 1
    return fib1
              
# Function to find and return the nth number in the Fibonacci Sequence
def fibonacciFinderN(n):
    fib0 = 0
    fib1 = 1    
    fib_count = 2
    while fib_count < n:
        temp = fib1
        fib1 = fib0 + fib1
        fib0 = temp
        fib_count += 1
    return fib1

# Tests
print(fibonacciFinder50())
print(fibonacciFinderN(300))