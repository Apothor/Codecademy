# Basic Difficulty
"""
Given two words (beginWord and endWord), and a dictionary’s word list, find the length of shortest transformation sequence from beginWord to endWord.
You may assume:
    Both beginWord and endWord are strings of equal length (that is, equal numbers of characters).
    beginWord and endWord are words with all lower-case characters (in ASCII hexadecimal, characters range from 61 to 7A)
    Letters cannot be inserted or deleted, only substituted.
    Only one letter can be changed at a time.
    Each intermediate word must exist in the word list.
    Your algorithm should be able to work with any dictionary, but for this challenge just use the one posted below. 
    Either copy it word for word into an array, or save it into a text file and load it using File I/O.
"""

def shortestTransformation(beginWord, endWord):
    dictionary = ['humic', 'humid', 'wane', 'jade', 'molt', 'moll', 'want', 'slag', 'wade', 
                  'mist', 'dolt', 'doll', 'mate', 'fade', 'maze', 'wart', 'jake', 'wary', 
                  'mitt', 'wake', 'gate', 'mite', 'wait', 'faze', 'malt', 'hemic', 'male']
    
    if beginWord not in dictionary:
        beginWord = input("""
            The first word provided does not exits in our dictionary.
            Please input a valid name from this list: {} """.format(', '.join(dictionary)))
    
    if endWord not in dictionary:
        endWord = input("""
            The first word provided does not exits in our dictionary.
            Please input a valid name from this list: {} """.format(', '.join(dictionary)))
        
                        
print(shortestTransformation("gate", "gate"))
