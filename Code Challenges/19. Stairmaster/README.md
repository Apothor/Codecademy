# This week’s challenge was reported to have been asked in interviews at **Facebook**.

## Basic difficulty

Write a function, `stairmaster20`, that will compute the number of ways to climb a flight of 20 steps, taking 1, 2, or 3 steps at a time.

* **Function Name**: `stairmaster20`
* **Inpu**: none
* **Output**: a positive integer representing the number of ways you can climb the flight of 20 stairs by climbing 1, 2, or 3 steps at a time.
* **Example**: say this problem were framed around climbing 4 steps – in this case `stairmaster4 => 7`, as there are seven different ways one can climb four stairs using a combination of climbing 1, 2, or 3 steps at a time are `([1,1,1,1] [2,1,1] [1,2,1] [1,1,2] [2,2] [1,3] [3,1])`
* In this challenge we are looking for a [permutation](https://betterexplained.com/articles/easy-permutations-and-combinations/), not a combination, as the order matters – climbing one step then two steps is different from climbing two steps then one step.
* What if your interviewer had follow-up questions, for example changing the number of floors to 50? What if you could now jump four steps at a time? Try to write your code so that it is easily read, easily maintained, and can be adapted to modifications in the interviewer’s questioning.
* Always remember to *explain*  your code and the thought processes behind it!

## Intermediate difficulty

Write a function, `stairmasterN`, that will compute the number of ways to climb a flight of n steps, taking 1, 2, or 3 steps at a time. Write stairmasterN *as efficiently as possible*.

* **Function Name**: `stairmasterN`
* **Input**: n – any positive integer
* **Output**: a positive integer representing the number of ways you can climb a flight of n stairs by climbing 1, 2, or 3 steps at a time.
* **Example**: `stairmasterN(4) => 7`
* Don’t forget to explain your submission just as you would do in a job interview setting!

## Hard difficulty

Write a function, ultimateStairmaster, that will compute the number of ways to climb a flight of n steps, taking x,y, …, z steps at a time. Write ultimateStairmaster as efficiently as possible.

* **Function Name**: `ultimateStairmaster`
* **Input**: n – any positive integer, `[x,y,.....,z]` - an array of integers, not necessarily in order, that has at least one number in but doesn’t have an upper limit.
* **Output**: a positive integer representing the number of ways you can climb a flight of n stairs by climbing `[x,y, …,z]` steps at a time.
* **Example**: `ultimateStairmaster(4, [1,2,3,4]) => 8`
* Don’t forget to explain your submission just as you would do in a job interview setting!
