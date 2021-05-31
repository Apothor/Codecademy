# Word Transformation

This week’s challenge was reportedly asked in interviews at Snap, Inc. (parent company of Snapchat)

## Basic Difficulty

Given two words (`beginWord` and `endWord`), and a dictionary’s word list, find the length of shortest transformation sequence from `beginWord` to `endWord`.

You may assume:

* Both `beginWord` and `endWord` are [strings](https://en.wikipedia.org/wiki/String_(computer_science)) of equal length (that is, equal numbers of [characters](https://en.wikipedia.org/wiki/Character_(computing)).
* beginWord and endWord are words with all lower-case characters (in [ASCII](https://en.wikipedia.org/wiki/ASCII) hexadecimal, characters range from 61 to 7A)
* Letters cannot be inserted or deleted, only substituted.
* Only one letter can be changed at a time.
* Each intermediate word must exist in the word list.
* Your algorithm should be able to work with any dictionary, but for this challenge just use the one posted [below](https://discuss.codecademy.com/t/challenge-word-transformation/84306/5?u=alexcraig). Either copy it word for word into an array, or save it into a text file and load it using File I/O.

## Intermediate difficulty

`beginWord` and `endWord` may now be strings of different lengths

You may assume:
Your function can now delete and insert letters.

## Hard Difficulty

Make your submission as efficient as possible.

* Try adding a timing function to your code, and try out different approaches to the problem to find the quickest solution. Also, try to reduce the amount of space you use.
*  You may limit your function to check whether the edit distance between beginWord and endWord is within some threshold or maximum distance of interest, k.
