# Basic difficulty
# Function that will return the missing number from a sequence of integers [1, 2, 3, …, 100].

# Naive solution.
def missingno(arr):
    
    arr.sort()
    
    # Traverse the array and return the index + 1 if the array does not match the index + 1.
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return i + 1
        
# Solution using set theory
def missingno(arr):
      
    nums = list(range(1, 101))
    nums = set(nums)
    arr = set(arr)
    return arr-nums
               
# Intermediate difficulty
# Function that will return the two missing numbers from a sequence of integers [1, 2, 3, …, 100].

# Naive solution.
def missingNOs(arr):
    
    # Initialize an array of integers [1, 2, 3, …, 100], 'nums' and an empty results array, 'found_nums'
    nums = list(range(1, 101))
    found_nums = []
    
    # Test this array against the input array.
    for num in nums:
       
        # If an integer is missing, add this integer to found_nums.
        if num not in arr:
            found_nums.append(num)
            
            # If two missing nubmers are found, return the numbers.
            if len(found_nums) == 2:
                return found_nums
            
# Solution using set theory
def missingno(arr):
      
    nums = [x for x in range(101)]
    nums = set(nums)
    arr = set(arr)
    return arr-nums

# Advanced difficulty
# Function that will return the k missing numbers from a bag of size n (array elements in range from 1 to n).

# Naive solution.
def missingNoKetsuban(k, n, arr):
    
    # Initialize an array of integers [1, 2, 3, …, 100], 'nums' and an empty results array, 'found_nums'
    nums = list(range(1, n))
    found_nums = []
    
    # Test this array against the input array.
    for num in nums:
       
        # If an integer is missing, add this integer to found_nums.
        if num not in arr:
            found_nums.append(num)
            
            # If two missing nubmers are found, return the numbers.
            if len(found_nums) == k:
                return found_nums
            

# More generalized solution that is ignorant about n.
def missingNoKetsuban(k, arr):
    
    arr.sort()
    arr.reverse()
    found_nums = []
    i = 0
        
    while len(arr) > k:
        i += 1  
        num = arr.pop()
        
        if num != i:
            found_nums.append(i)

        while num != i:
            i += 1

    return found_nums

# More generalized solution that is ignorant about n or k.
def missingNoKetsuban(arr):
    
    arr.sort()
    arr.reverse()
    found_nums = []
    i = 1
    
    while arr:
        num = arr.pop()
        if num != i:
            found_nums.append(i)
        while num != i:
                i += 1

    return found_nums

# Optimized solution that is ignorant about n or k.
def missingNoKetsuban(k, n, arr):
    found_nums = []
    arr_set = set(arr)
    for num in range(1, n+1):     
        if not num in arr_set:
            found_nums.append(num)
            if len(found_nums) == k:
                return found_nums
            
# Optimized solution using set theory.
def missingNoKetsuban(arr): 
    n = max(arr)
    nums = [x for x in range(1, n+1)]
    nums = set(arr)
    arr = set(arr)
    return nums - arr

# Another solutiom.
def missingNoKetsuban(n, arr):
    n = max(arr)
    arr = set(arr)
    for num in range(1, n+1):
        if not num in arr:
            found_nums.append(num)
    return found_nums