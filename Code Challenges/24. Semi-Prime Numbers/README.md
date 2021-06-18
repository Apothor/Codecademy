# Semi-Prime Numbers

## Basic difficulty

Write a function, `semiPrimeDetector`, that tests if a number, n is a [semi-prime](https://en.wikipedia.org/wiki/Semiprime) number.

* **Function Name**: `semiPrimeDetector`
* **Input**: integer n
* **Output**: boolean: true if n is a semi-prime number else false.
* **Example**: `semiPrimeDetector(194)` => True

## Intermediate difficulty

Write a function, `semiPrimeCount`, that will print total number of semi-prime numbers below a number, n.

* **Function Name: `semiPrimeCount`
* **Input**: integer n
* **Output**: An integer c, count of all the semi-prime numbers below n.
* **Example**: `semiPrimeCount(30)` will output 10, which includes semi-prime numbers - `[4, 6, 9, 10, 14, 15, 21, 22, 25, 26]`.

## Hard difficulty

Write `semiPrimeDetector` and `semiPrimeCount` *as efficiently as possible*.

## Extra

Write a function to check if the output of `semiPrimeCount` is odd or even.
* **Output**: 0 if `semiPrimeCount` output an even number, 1 if the output is odd
* **Example**: `semiPrimeCount(30)` will output 10, so this function should output 0
* Try to solve this without using `semiPrimeCount`.
