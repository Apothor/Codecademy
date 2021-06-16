# Flatten an Array

This week’s challenge was reported to have been asked in interviews at **Facebook** and has also been asked right here at Codecademy!

## Basic difficulty

Write a function, `flattenArray`, that when given an [2D](https://www.sparknotes.com/cs/arrays/2darrays/summary/) array, flattens it into a [1D](https://www.sparknotes.com/cs/arrays/1darrays/summary/) array

* **Function Name**: `flattenArray`
* **Input**: a 2D array
* **Output**: a 1D array
* **Example**: `flattenArray([1,2,3, [4,5], 6, [7,8], 9])` => `[1,2,3,4,5,6,7,8,9]`
* Always remember to explain your code and the thought processes behind it!
* You can think of a 2D array as a spreadsheet or a chessboard, whereas a 1D array is more like a list or one long chain of data.
* What if your interviewer had follow-up questions or extensions to this challenge? Don’t anticipate what exactly those follow-ups or changes may be, but try to write your code so that it is easily read, easily maintained, and can be adapted to potential modifications in the interviewer’s questioning.

## Intermediate difficulty

Improve on the `flattenArray` function by writing `flattenArrayN`, a function that can flatten arrays that are nested n-levels deep, returning a flattened 1D array.

* **Function Name**: `flattenArrayN`
* **Input**: any array with n levels of depth, where n is an integer ≥1
* **Output**: a 1D array
* **Example**: `flattenArrayN([1, 2, [3, [4, 5]], 6])` => `[1, 2, 3, 4, 5, 6]`
* For our intermediate challenge, the array can have multiple types: {}, [], "", undefined, null, and integers (1,2,3,…) are all valid types inside the array.
* You must explain your submission to be able to win!

## Hard difficulty

Write `flattenArray` and `flattenArrayN` *as efficiently as possible*.
