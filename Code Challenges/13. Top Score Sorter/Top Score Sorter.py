# Function to sort a list of scores and a high_score in descending order and return the sorted list
def scoreSettler(list_of_scores, high_score):
    
    # Helper function to perform a quicksort
    def quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quickSort(array, low, pi - 1)
            quickSort(array, pi + 1, high)
            
    # Help function to find the partition position
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    # Perform a quickSort of the list_of_scores
    quickSort(list_of_scores, 0, len(list_of_scores) - 1)
    
    # Return the high_score and the reversed sorted list 
    return [high_score] + list_of_scores[::-1]


# Tests
# scoreSettler([ 1, 2, 3, 999999], 1000000) => [999999, 3, 2, 1]
print(scoreSettler([ 1, 2, 3, 999999], 1000000)) 
# scoreSettler([874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100], 1218000)
print(scoreSettler([874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100], 1218000))