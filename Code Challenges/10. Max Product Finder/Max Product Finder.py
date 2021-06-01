'''
Max Product Finder

This week’s challenge was reported to have been asked in interviews at Google

Basic Difficulty

Given an array of integers, write a function, maxProductFinder, that finds the largest product that can be obtained from any 3 integers in the array.

    Function Name: maxProductFinder
    Input: int[] - an array of integers
    Output: an integer – the maximum product found from any three integers in the array
    Example: maxProductFinder([-8, 6, -7, 3, 2, 1, -9]) => 432
    You may assume that the array contains at least three integers
    Please run the following array as a test: [-6, -8, 4, 2, 5, 3, -1, 9, 10]

Intermediate difficulty

Given an array of integers, write a function, maxProductFinderK, that can be obtained from any k integers in the array.

    Function Name: maxProductFinderK
    Input: int[] - an array of integers and an integer k where k is the number of ints that can be used
    Output: an integer – the maximum product found from any k integers in the array
    Example: maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 2) => 72
    You may presume that the length of the array of integers is greater or equal to k
    
Hard Difficulty

Write maxProductFinder and maxProductFinderK as efficiently as possible.

'''

# Basic difficulty

# maxProductFinder(arr) finds and returns the largest product that can be obtained from any 3 integers in an array
def maxProductFinder(arr):
    from itertools import combinations
    from functools import reduce
    integer_combinations = combinations(arr, 3)
    max_product = 0
    for combination in integer_combinations:
        integer_product = reduce(lambda a, b: int(a)*int(b), combination)
        if integer_product > max_product:
            max_product = integer_product
    return max_product

# Tests
# maxProductFinder([-8, 6, -7, 3, 2, 1, -9]) => 432
print(maxProductFinder([-8, 6, -7, 3, 2, 1, -9]))


# Intermediate difficulty

# maxProductFinderK(arr, k) finds and returns the largest product that can be obtained from any k integers in the array.
def maxProductFinderK(arr, k):
    from itertools import combinations
    from functools import reduce
    integer_combinations = combinations(arr, k)
    max_product = 0
    for combination in integer_combinations:
        integer_product = reduce(lambda a, b: int(a)*int(b), combination)
        if integer_product > max_product:
            max_product = integer_product
    return max_product

# Hard difficulty

# maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 2) => 72
print(maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 2))

# Hard Difficulty
# maxProductFinderK(arr, k) finds and returns the largest product that can be obtained from a given number of integers in an array
def maxProductFinderK(arr, k):
    negative_arr = sorted([x for x in arr if x < 0])
    positive_arr = sorted([x for x in arr if x > 0])[::-1]
    max_product = 1
    while k >= 2:
        negative_product = negative_arr[0] * negative_arr[1]
        positive_product = positive_arr[0] * positive_arr[1]
        if positive_product > negative_product:
            max_product *= positive_product
            positive_arr.pop(0)
            positive_arr.pop(0)
        else:
            max_product *= negative_product
            negative_arr.pop(0)
            negative_arr.pop(0)
        k -= 2
    if k == 1:
        max_product *= positive_arr[0]
    return max_product
    
# Tests
# maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 2) => 72
print(maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 2))
# maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 3) => 432
print(maxProductFinderK([-8, 6, -7, 3, 2, 1, -9], 3))