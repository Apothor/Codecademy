# Build and Test Balance of a Binary Search Tree

## Easy difficulty

You are given a list of numbers stored in a list, A. Your challenge is to build a [Binary Search Tree] (Binary search tree - Wikipedia 288) to store these numbers. You will need to:

1. Represent each node of the tree (including its data, left child and right child).
2. Print the tree out in an understandable form.
3. Make a function to insert a list of numbers (A) into the tree.

Check if you can insert all the numbers in A into your tree, and that it prints out as expected.
Use the language of your choice to solve this challenge, but only submissions in languages taught by Codecademy are eligible to “win”.

## Intermediate difficulty

1. Write a function to check if the Binary Search Tree that you’ve created is balanced.
A tree is considered balanced when the difference between the min depth and max depth does not exceed 1, i.e. if the list had n elements in it the height of the tree would be log(n) (base 2).



## Hard Difficulty

1. Adapt your function to insert a list of n numbers so that it runs in O(n log n) time. Bear in mind that this is just the average case for a random sequence of numbers. If the list A was sorted it would take O(n^2).
2. Adapt your function to check if the tree is balanced so that it runs in O(n) time.
3. If your BST is balanced then the insert function would have only taken O(n log n) time, see if you can figure out why.

Find out more about the challenges[https://discuss.codecademy.com/t/essential-information-on-code-challenges/83909#hard] 
