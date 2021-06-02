# Select a number, any number

This week’s challenge was reported to have been asked in interviews at **Amazon**.

## Basic difficulty

Write a function, `getMedian`, that will return the median value of a list of numbers.

* **Function Name**: `getMedian`
* **Input**: An unsorted List of integers
* **Output**: The integer which is the median value of the input list.
* **Examples**: `getMedian([6,10,2,5,9,3,10,12,18,-3]) => 7.5` (average of the middle two values)
`getMedian([5,10,-3,7,9]) => 7`

## Intermediate difficulty

Write a function, getX, that given an integer x and a list returns the Xth number if the list was in sorted order.

* **Function Name**: `getX`
* **Input**: An integer, x, and an unsorted list of integers
* **Output**: The integer corresponding to the Xth number in the sorted list
* **Example**: `getX(2, [5,10,-3,7,9]) => 5`
getX(4, [5,10,-3,7,9]) => 9
Note that this assumes the first number is position 1 not 0.

## Hard difficulty

Write `getX` so that the list is not simply sorted and then the Xth element picked out. It is possible to solve this problem in linear time, O(n).
