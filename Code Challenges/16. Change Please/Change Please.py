# Function that will return the number of possible ways in which an amount of money can be broken down into change
# This solution will use abootom-up dynamic programming approach
def changeOptions(n, S):
    m = len(S)
    
    # Initialize an array to store the solutions to the problem:
    # The number of possible ways in which any amount of money up to and including n can be broken down into change 
    A = [0 for _ in range(n+1)]
  
    # Base case
    A[0] = 1
  
    # Pick all coins one by one and update the values in A
    # after the index greater than or equal to the value of the picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            A[j] += A[j - S[i]]
  
    return A[n]

# Driver program to test above function(s)
S = [x*y for x in [10**x for x in range(5)] for y in [1, 2, 5]]
print(changeOptions(5, S) == 4)
print(changeOptions(6, S) == 5)
print(changeOptions(7, S) == 6)
print(changeOptions(8, S) == 7)
print(changeOptions(10, S) == 11)

# This code was written by Tim Vlek