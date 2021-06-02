# Product of Everything Else

This week’s challenge was reported to have been asked in interviews at **Google**.

## Basic difficulty

Write a function, `productOfTheOthers` that, when given an array of n integers, replaces each number in the array with the product of all the numbers in the array except the number itself.

for example, when given the array `[1,2,3,4]`, `productOfTheOthers` would return `[24, 12, 8, 6]`
* **Function Name**: productOfTheOthers
* **Input**: an array – for your submission use the test array `[3, 9, 7, -2]`
* **Output**: an array – when given the test array, your submission should return `[-126, -42, -54, 189]`
* **Example**: `productOfTheOthers([3, 9, 7, -2]) => [-126, -42, -54, 189]`
* Your array may have n integers, presume that n > 1.
* Would your function work if the input array contained zeroes?

## Intermediate difficulty

Solve the basic challenge, but this time do so *without using division*. Call this new function `advProductOfTheOthers`.

* **Function Name**: `advProductOfTheOthers`
* **Input**: an array – for your submission use the test array `[0, 9, 7, 8, -2]`
* **Output**: an array
* **Example**: `advProductOfTheOthers([1,2,3,4]) => [24, 12, 8, 6]`

## Hard difficulty

Write `advProductOfTheOthers` *as efficiently as possible*.
