# Find the Missing Number

This week’s challenge was reported to have been asked in interviews at **Twitter**:

# Basic difficulty

You have a bag containing tiles with numbers [1, 2, 3, …, 100] written on them. Each number appears exactly once, so there are 100 tiles and 100 numbers. Now, without looking, one number tile is randomly picked out of the bag and discarded. Write a function, `missingNo`, that will find the missing number.

* **Function Name**: `missingNO`
* *** **Input**: an array, [1, 2, …, 100] with one number between 1 and 100 missing.
* **Output**: an integer, the “missing” number in the array
* **Example**: missingNo([1, 3, …, 100]) => 2 if the array was missing the number 2. Please include in your submission a test array with number 66 missing.
* The array may not be sorted.
* The removal of a number from the bag is totally random, there is no way to tell what number it was by the process of removing it (e.g. you cannot feel what number is written on the tile)
* You may look in the bag of number tiles and interact with the contents once the random number is removed. So, you can lay all of the tiles out,
* Always remember to explain your code and the thought processes behind it!
* What if your interviewer had follow-up questions or extensions to this challenge? Don’t anticipate what exactly those follow-ups or changes may be, but try to write your code so that it is easily read, easily maintained, and can be adapted to potential modifications in the interviewer’s questioning.

## Intermediate difficulty

You replace the missing number in the bag, so you again have 100 tiles numbered from 1 to 100. This time, you remove two random number tiles. Write a function, `missingNOs`, that will find the missing numbers.

* **Function Name**: missingNOs
* **Input**: an array, [1, 2, …, 100] with two numbers between 1 and 100 missing.
* **Output**: an array of two integers, showing both “missing” numbers in the array in any order
* **Example**: missingNOs([1,4, …, 100) => [2, 3]
* Do you have to write a second script (i.e. write another version of missingNO to solve this challenge, or could you simply generalize what you’ve made in the basic challenge?
You must explain your submission to be able to win!

## Hard difficulty

Write a function, `missingNoKetsuban`, that will efficiently solve for a bag of size n (array elements in range from 1 to n) exactly k numbers missing from the bag.

You could think of this as a generalization of what you’d learn by solving the basic and intermediate level challenges.
Don’t forget to explain your submission just as you would do in a job interview setting!
