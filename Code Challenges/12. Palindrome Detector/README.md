# Palindrome Detector

This week’s challenge was reported to have been asked in interviews at **Facebook**:

## Basic Difficulty

Write a function, `isPermPalindrome`, that will test if a given string is a permutation of a palindrome.

* **Function Name**: `isPermPalindrome`
* **Input**: a `String` consisting only of lowercase letter characters
* **Output**: a `boolean, true` if the string is a permutation of a palindrome and `false` if the string is not a permutation of a palindrome
* **Examples**:
  * `isPermPalindrome("kayak") => true`
  * `isPermPalindrome("yakak") => true`
* [Permutations](https://www.mathsisfun.com/definitions/permutation.html) 40 are all possible arrangements of a collection of things, where the order is important.
* From Merriam Webster, a palindrome is a “word, verse, or sentence (such as “Able was I ere I saw Elba”) or a number (such as 1881) that reads the same backward or forward.” Read more about palindromes here 10 or see some interesting examples here 27.

## Intermediate difficulty

As above, but isPermPalindrome should now be able to account for punctuation, spaces, and capitalization in the input string.

Your input string may now include spaces, numbers, punctuation, and capitalization, but in assessing whether the string is a palindrome or not, spaces, punctuation, and capitalization does not matter. For example, akyKa is a permutation of Kayak, but we don’t care that there is one upper case K and one lower case k in Kayak – this is still a palindrome.
* **Example**: isPermPalindrome("Science Bros.") => false

## Hard Difficulty

Write `isPermPalindrome` as efficiently as possible.
