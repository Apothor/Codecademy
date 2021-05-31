# Easy difficulty
""" Write a function that will take a given string and reverse the order of the words. 
“Hello world” becomes “world Hello” and “May the Fourth be with you” becomes “you with be Fourth the May” """

def reverse_words(s):
    return ' '.join(s.split(' ')[::-1])

# Intermediate difficulty
"""The string in question now has punctuation, for example “Hello world!” and “With you, be May the Fourth”.
Write a function to reverse the order of words, but keep the punctuation in place. 
For example, turn "Hello world!" into “world Hello!” and “With you, be May the Fourth.” to “Fourth the, May be you With.”
In the case of multiple consecutive punctuation marks or multiple consecutive whitespace characters, deal with them as you see fit."""

def reverse_words(s):
    words = s.split(' ')
    punctuation_pattern = '[.,;:!?]+$'
    punctuation_indices = []
    punctuation_symbols = []
           
    for i in range(len(words)):       
        search = re.search(punctuation_pattern, words[i])
        if search is not None:
            punctuation_indices.append(i)
            punctuation_symbol = search.group(0)
            punctuation_symbols.append(punctuation_symbol)
            words[i] = words[i].replace(punctuation_symbol, '')
            
    words = words[::-1]
    
    for i in punctuation_indices:
        words[i] = words[i] + punctuation_symbols.pop(0)
        
    return ' '.join(words)

# Hard difficulty
"""
Can you solve the initial challenge (without punctuation) in-place without using additional data structures, and with the time complexity being O(n)?
Can you do the same for the intermediate level challenge (including punctuation)?
"""

# TODO
"""
def reverse_words(s):  
          
    # Initialize parameters
#     s = [c for c in s]
    left_index = 0
    right_index = len(s) - 1

    left_character = ''
    right_character = ''
    left_word = ''
    right_word = ''
    left_punctuation = ''
    right_punctuation = ''
    left_state = 0
    right_state = 0
    
    while left_index < right_index:
        
        if left_character == ' ':
            while right_character != ' ':
                
                if right_character in '.,;:!?':
                    right_punctuation += right_character
                    print('right_punctuation', ''.join(right_punctuation))

                else:
                    right_word = right_character + right_word
                    print('right_word', right_word)
                    
                right_character = s[right_index]
                s = s[:right_index] + s[right_index + 1:]
                
                right_index -= 1
            
            print(left_index)
            left_punctuation += left_character
            
            s = (
                s[:left_index] + 
                right_word + 
                left_punctuation + 
                s[left_index:right_index + 1] + 
                right_character + 
                left_word + 
                right_punctuation + 
                s[right_index + 1:])
            
            left_index += len(left_punctuation + right_word)
            print(left_index)
            right_index += len(left_punctuation + right_word)
            print(right_index)
            
            right_word = ''      
            left_word = ''
            left_punctuation = '' 
            right_punctuation = ''
            
            print(s)
            print(left_index)
            
            right_character = s[right_index]
            s = s[:right_index] + s[right_index + 1:]   
            right_index -= 1


        elif left_character in '.,;:!?':
            left_punctuation += left_character
            print('left_punctuation', left_punctuation)

        else:
            left_word += left_character
            print('left_word', left_word)
       
        left_character = s[left_index]
        s = s[:left_index] + s[left_index + 1:]     
        print(s)
        right_index -= 1

    return ''.join(s)
                
            
print(reverse_words('With you, be May the Fourth.')) 