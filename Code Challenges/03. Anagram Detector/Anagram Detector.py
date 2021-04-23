# Easy difficulty
# Write a function in your favorite programming language that will accept any two strings as parameters and return “1” if they are anagrams and “0” if they are not.

def anagram_detector(s, s2):
    if s.lower()[::-1] == s2.lower():
        return 1
    else:
        return 0

# Intermediate difficulty
# Make sure that your answer has no more than O(n + m) time complexity 65, where n is the length of the first string and m of the second.

def anagram_detector(s, s2):
    anagram = True
    i = 1
    while anagram:
        try:
            if s[i-1].lower()  == s2[-i].lower():
                i += 1
            else:
                return 0
        except:
            return 1