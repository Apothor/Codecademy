# Function that replaces each number in an array with the product of all the numbers in the array except the number itself
def productOfTheOthers(array):
    from functools import reduce
    product = reduce(lambda x,y: x*y if x != 0 and y!= 0 else 0, array)
    array = [product//x if x !=0 else 0 for x in array ]
    return array

# Function (optimized not using module imports) identical to the original productOfTheOthers()
def productOfTheOthers(array):
    product = 1
    for x in array:
        product *= x
    array = [product//x if x !=0 else 0 for x in array ]
    return array

# Function that replaces each number in an array with the product of all the numbers in the array except the number itself without using division
def advProductOfTheOthers(array):
    from functools import reduce
    result = []
    for _ in range(len(array)):
        arr2 = array.copy()
        arr2.pop(_)
        x2 = reduce(lambda x,y: x*y, arr2)
        result.append(x2)
    return result

# Function (optimized not using module imports) identical to the original advProductOfTheOthers()
# Take note: productOfTheOthers is FASTER!
def advProductOfTheOthers(array):
    result = []
    length = len(array)
    length2 = length - 1
    for _ in range(length):
        arr2 = array.copy()
        arr2.pop(_)
        x2 = 1
        for j in arr2:
            x2 *= j
        result.append(x2)
    return result

# Tests
print(productOfTheOthers([3, 9, 7, -2]) == [-126, -42, -54, 189])
print(advProductOfTheOthers([1,2,3,4]) == [24, 12, 8, 6])
print(advProductOfTheOthers([0, 9, 7, 8, -2]) == [-1008, 0, 0, 0, 0])