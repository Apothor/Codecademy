# Function to find and return the median value of a list of numbers
def getMedian(list_of_integers):
    from statistics import median
    return median(list_of_integers)

# Function to find and return the Xth number if the list was in sorted order
def getX(x, list_of_integers):
    list_of_integers.sort()
    return list_of_integers[x - 1]

# TO DO. Use 'Meidum of Mediums'
def mOfMs(i, A, x = 5):
    if len(A) <= x :
        A.sort()    # this runs in linear time for 5 items
        return A[i]
    M = [mOfMs(x//2, A[a:a+x], x) for a in range(0,(len(A)//x)*x, x)]
    M = mOfMs(len(M)//2, M, x)
    A.remove(M)
    left, right = [x for x in A if x<=M], [x for x in A if x>M]
    if i == len(left):
        return M
    return mOfMs(i-(len(left)+1), right, x) if i>len(left) else mOfMs(i, left, x)
    

# Tests
# getMedian([6,10,2,5,9,3,10,12,18,-3]) => 7.5
print(getMedian([6,10,2,5,9,3,10,12,18,-3]) == 7.5)
# getMedian([5,10,-3,7,9]) => 7
print(getMedian([5,10,-3,7,9]) == 7)
# getX(2, [5,10,-3,7,9]) => 5
print(getX(2, [5,10,-3,7,9]) == 5)
# getX(4, [5,10,-3,7,9]) => 9
print(getX(4, [5,10,-3,7,9]) == 9)

print(mOfMs(4, [5,10,-3,7,9]))
print(mOfMs(4, [1,24,23,4,22, 101,105,123, 19,6,7,8,9,10,11,12,13, 14, 15]))