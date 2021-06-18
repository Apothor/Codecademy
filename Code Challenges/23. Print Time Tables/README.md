# Print Time Tables

This week’s challenge was reported to have been asked in interviews at **Google**:

# Basic difficulty

Write a function, `timesTables`, that prints out multiplication tables (the type you learned in primary / grade school) up to 12x12.

* **Function Name**: `timesTables`
* **Output**: Example output:

`1 2 3 4 5 6 7 8 9 10 11 12
2 4 6 8 10 12 14 16 18 20 22 24
3 6 9 12 15 18 21 24 27 30 33 36
4 8 12 16 20 24 28 32 36 40 44 48
5 10 15 20 25 30 35 40 45 50 55 60
6 12 18 24 30 36 42 48 54 60 66 72
7 14 21 28 35 42 49 56 63 70 77 84
8 16 24 32 40 48 56 64 72 80 88 96
9 18 27 36 45 54 63 72 81 90 99 108
10 20 30 40 50 60 70 80 90 100 110 120
11 22 33 44 55 66 77 88 99 110 121 132
12 24 36 48 60 72 84 96 108 120 132 144`

* This challenge may appear to be quite easy, and part of the point of many code challenges asked in interviews is that they *are* easy (see [here](https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions))! You should be able to solve this in under ten minutes. How elegantly can you write your solution? Plan your strategy for solving this question and walk your “interviewer” through your thought processes (that is, write down an explanation for your code and your thinking behind it). What’s the *best* way to solve this problem? What are some interesting *non-standard* approaches to solving this problem?
* What if your interviewer had follow-up questions or extensions to this challenge? Don’t anticipate what exactly those follow-ups or changes may be, but try to write your code so that it is easily read, easily maintained, and can be adapted to potential modifications in the interviewer’s questioning.

## Intermediate difficulty

Write a function, `oddTimesTables`, that will print *only the odd numbers* from the multiplication tables up to 12x12.

* **Function Name**: oddTimesTables
* **Output**:
`1 3 5 7 9 11
3 9 15 21 27 33
5 15 25 35 45 55
7 21 35 49 63 77
9 27 45 63 81 99
11 33 55 77 99 121`

* You can reason which numbers will be odd based on the patterns in multiplication tables, but whatever method you choose, you should also write a test that makes sure that the numbers to be printed are indeed odd.

## Hard difficulty

Write `timesTables` and `oddTimesTables` *as efficiently as possible*.
