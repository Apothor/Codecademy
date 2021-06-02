# Basic difficulty

# Function that will test if a given string is a permutation of a palindrome.
def isPermPalindrome(s):
    character_counts = {}
    for k in s:
        if k not in character_counts:
            character_counts[k] = True
        else:
            del character_counts[k]           
    return sum(character_counts.values()) in [0, 1]

# Intermediate difficulty

# Function that will test if a given string is a permutation of a palindrome, while ignoring spaces, punctuation and capitalization
def isPermPalindrome(s):
    import string
    s = "".join(s.split())
    s = "".join(s.split(string.punctuation))
    s.lower()
    character_counts = {}
    for k in s:
        if k not in character_counts:
            character_counts[k] = True
        else:
            del character_counts[k]           
    return sum(character_counts.values()) in [0, 1]

# Tests
# isPermPalindrome("kayak") => true
print(isPermPalindrome("kayak"))
# isPermPalindrome("yakak") => true
print(isPermPalindrome("yakak"))
# isPermPalindrome(".mqwkcgv ibqwelfi02387653909nkxc . ") => false
print(isPermPalindrome(".mqwkcgv ibqwelfi02387653909nkxc . "))
# isPermPalindrome("Science Bros.") => false
print(isPermPalindrome("Science Bros."))