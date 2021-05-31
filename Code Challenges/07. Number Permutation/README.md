# Number Permutation

## Basic Difficulty

Create a program makeNumberBasic(z) which, when given an input of a number (z), returns the number of all possible permutations of digits (1 through 9 inclusive) that when added will equal z.

More details:
* For example, if z is 3, your program will find that four permutations of digits add up to that value (3, 2+1, 1+1+1, and 1+2), and thus return 4.
* You may limit makeNumberBasic(z) to the use of five digits
* Repeat use of a digit is acceptable: e.g. 1+1+1 would be a valid addition of digits equalling 3.
* Use of a single digit is acceptable as a permutation: e.g. 3 is itself a valid permutation of digits that add up to 3.
* makeNumberBasic(z) is looking for permutations 15, not combinations 5: 1+5 and 5+1 would count as two unique possible ways to add to 6, not one. Read more about permutations vs. combinations here 15.
* If no permutations of the digits 1 through 9 add up to the number z, your function should return 0.

## Intermediate difficulty

Write makeNumber(z) so that it only returns the number of combinations of unique digits from 1 to 9.

* For example, if z is 3, your program will find the unique combinations 3 and 1+2, and thus return 2.
* To clarify unique digits: repeat use of a digit is no longer acceptable. 1+5, 1+2+3, 2+4, and 3+3 all equal 6, but makeNumber(z) would not consider 3+3 a valid combination as it uses the digit 3 more than once. 
* makeNumber(z) is now looking for combinations 3 not permutations: 1+5 and 5+1 would now only be accepted as one possible way to add digits 1 through 9 to 6, not two.

## Hard Difficulty

Write versions of makeNumberBasic(z) and of makeNumber(z) (the normal and intermediate difficulty challenges) as efficiently as possible.

[Our sample solution](https://replit.com/@AlexJC/Make-Number)
