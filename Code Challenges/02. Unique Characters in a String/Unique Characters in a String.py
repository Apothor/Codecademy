# Easy difficulty
# Write a function that determines if any given string 433 has all unique characters 191 (i.e. no character in the string is duplicated). 
# If the string has all unique characters, print “all unique”. 
# If the string does not have all unique characters, print “duplicates found.”

def unique_characters(s):
    from collections import Counter
    c = Counter(s)
    if sum(c.values()) == len(c.values()):
        return "all unique"
    else:
        return "duplicates found"
        
# Intermediate difficulty
# Don’t use any additional data structures.

def unique_characters(s):
    if len(set(s)) == len(s):
        return "all unique"
    else:
        return "duplicates found"
    
# Alternatively       
def unique_characters(s):
    unique_chars = []
    for char in s:
        if char in unique_chars:
            return "duplicates found"
        else:
            unique_chars.append(character)
    return "all unique"