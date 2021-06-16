# Basic Difficulty

'''
Write a function, flattenArray, that when given an 2D array, flattens it into a 1D array

    Function Name: flattenArray
    Input: a 2D array
    Output: a 1D array
    Example: flattenArray([1,2,3, [4,5], 6, [7,8], 9]) => [1,2,3,4,5,6,7,8,9]
    Always remember to explain your code and the thought processes behind it!
    You can think of a 2D array as a spreadsheet or a chessboard, whereas a 1D array is more like a list or one long chain of data.

What if your interviewer had follow-up questions or extensions to this challenge? 
Don’t anticipate what exactly those follow-ups or changes may be, but try to write your code so that it is easily read, easily maintained, and can be adapted to potential modifications in the interviewer’s questioning.
'''

# A solution using 'isinstance' to check for nested lists.
def flattenArray(inputArray):
    result = []
    for element in inputArray:
        if isinstance(element, list):
            for item in element:
                result.append(item)
        else:
            result.append(element)
    return(result)

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

# A solution using 'type' to check for nested lists.
def flattenArray(inputArray):
    result = []
    for element in inputArray:      
        result += element if type(element) is list else [element]
    return result

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

# A solution using try/except.
def flattenArray(inputArray):
    result = []
    for element in inputArray:
        try:
            result.extend(element)
        except:
            result.append(element)
    return(result)

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

# Intermediate difficulty

''' 
Improve on the flattenArray function by writing flattenArrayN, a function that can flatten inputArrays that are nested n-levels deep, returning a flattened 1D inputArray.

Function Name: flattenArrayN
Input: any inputArray with n levels of depth, where n is an integer ≥1
Output: a 1D inputArray
Example: flattenArrayN([1, 2, [3, [4, 5]], 6]) => [1, 2, 3, 4, 5, 6]
For our intermediate challenge, the inputArray can have multiple types: {}, [], "", undefined, null, and integers (1,2,3,…) are all valid types inside the inputArray.
You must explain your submission to be able to win!
'''

# Below I provide some solutions that handle empty values and strings differently.

# A recursive solution using isinstance to check and convert arrays into iterables.
# This solutions keeps empty strings and strings consisting of spaces only.
# Alternatively one could convert everything into lists or tuples.
# The else clause should be redundant, considering all mentioned cases are covered in the if/elif statements.
def flattenArrayN(inputArray):
    result = []
    if isinstance(inputArray, int):
        result.append(inputArray)
    elif isinstance(inputArray, str):
        result.append(inputArray)
    elif isinstance(inputArray, tuple):
        for element in inputArray:
            result += flattenArrayN(element)
    elif isinstance(inputArray, dict):
        for element in iter(inputArray.items()):
            result += flattenArrayN(element)
    elif isinstance(inputArray, list):
        for element in iter(inputArray):
            result += flattenArrayN(element)
    else:
        result.append(inputArray)
    return result

print(flattenArrayN([1, ['', (' ', {'test': None})]]))

# A creative solution using string replacement.
# This solutions discards empty strings and strings consisting of spaces only.
def flattenArrayN(inputArray):
    inputString = str(inputArray).replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace(',', ' ').replace(':', ' ').replace('\'', '')
    inputList = inputString.split()
    result = []
    for element in inputList:
        try:
            result.append(eval(element))
        except:
            result.append(element)
    return result

print(flattenArrayN([1, ['', (' ', {'test': None})]]))

# A solution using hasattr.
# This solutions flattens strings, while discarding empty strings, but keeping strings consisting of spaces only.
def isIterable(anyObject): 
    if hasattr(anyObject, '__iter__'):
        if not len(anyObject):
            return True
        elif len(anyObject) > 0:
            if not next(iter(anyObject)) == anyObject:
                return True
    else:
        return False

def flattenArrayN(inputArray):
    result = []
    for element in inputArray:        
        if isIterable(element):
            result += flattenArrayN(element if type(element) is not dict else element.items())  
        else:
            result.append(element)
    return result

print(flattenArrayN([1, ['', (' ', {'test': None})]]))

# Hard Difficulty

'''
Write flattenArray and flattenArrayN as efficiently as possible.
Don’t forget to explain your submission just as you would do in a job interview setting!
'''

# Space efficient solutions for the three flattenArray solutions.

# An in-place solution with O(n) using 'isinstance' to check for nested lists.
def flattenArray(inputArray):
    for _ in range(len(inputArray)):
        element = inputArray.pop(0)
        if isinstance(element, list):
            for item in element:
                inputArray.append(item)
        else:
            inputArray.append(element)
    return(inputArray)

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

# An in-place solution with O(n) using 'type' to check for nested lists.
def flattenArray(inputArray):
    for _ in range(len(inputArray)):
        element = inputArray.pop(0)
        inputArray += element if type(element) is list else [element]
    return inputArray

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

# An in-place solution with O(n) using try/except.
def flattenArray(inputArray):
    for _ in range(len(inputArray)):
        element = inputArray.pop(0)
        try:
            inputArray.extend(element)
        except:
            inputArray.append(element)
    return(inputArray)

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))
    
# Space efficient solutions for the two flattenArrayN solutions.
# TO DO!!!
# def flattenArrayN(inputArray):
#     inputArray = iter(inputArray)
#     while True:
#         try:
#             element = next(inputArray)
#             if isinstance(inputArray, int):
#                 result.append(inputArray)
#             elif isinstance(inputArray, str):
#                 result.append(inputArray)
#             elif isinstance(inputArray, tuple):
#                 for element in inputArray:
#                     result += flattenArrayN(element)
#             elif isinstance(inputArray, dict):
#                 for element in iter(inputArray.items()):
#                     result += flattenArrayN(element)
#             elif isinstance(inputArray, list):
#                 for element in iter(inputArray):
#                     result += flattenArrayN(element)
# #             else:
# #                 result.append(inputArray)
#         except:
#             return list(inputArray)
        
# print(flattenArrayN([1, 2, [3, [4, 5]], 6, (1, 'b'), '', (), ' ', None,  {'b': 5}]))  

# An in-place solution with O(n) using string replacement.
# This solutions discards empty strings.
def flattenArrayN(inputArray):
    inputArray = str(inputArray).replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace(',', ' ').replace(':', ' ').replace('\'', '')
    inputArray = inputArray.split()
    for _ in range(len(inputArray)):
        element = inputArray.pop(0)
        try:
            inputArray.append(eval(element))
        except:
            inputArray.append(element)
    return inputArray

print(flattenArrayN([1, ['', (' ', {'test': None})]]))

# An in-place solution with O(n) using hasattr.
# This solutions flattens strings, while discarding empty strings and keeping strings consisting of spaces only.
def isIterable(anyObject): 
    if hasattr(anyObject, '__iter__'):
        if not len(anyObject):
            return True
        elif len(anyObject) > 0:
            if not next(iter(anyObject)) == anyObject:
                return True
    else:
        return False
       
def flattenArrayN(inputArray):
    result = []
    for  element in inputArray:   
        if isIterable(element):
            result += flattenArrayN(element if type(element) is not dict else element.items())  
        else:
            result.append(element)
    return result

print(flattenArrayN([1, ['', (' ', {'test': None})]])) 