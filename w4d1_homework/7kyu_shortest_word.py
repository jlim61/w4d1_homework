'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''


'''
Brainstorm/Notes

strings will NEVER be empty, so no edge case in that sense. Do NOT need to account for different data types so I am only working with strings
I need to return the length of the shortest word in a string of words

I think I might have to use a for loop to iterate over the entire string. I can convert it to a list so that I can have each word be an element. A split function could help with this.

I need something to hold all the lengths while I iterate through this so maybe set an empty list to append the lengths to.
'''

example_list = 'bitcoin take over the world maybe who knows perhaps'

# link: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

# defining my function
def find_short(s):
#     printing s just for visuals, uncomment line below to see
#     print(s)
# setting s to s.split() so that I can make each word an element in a list
    sentence = s.split()
#     printing s just for visuals, uncomment line below to see
#     print(s)
# setting an empty list to grab length of words
    word_lengths = []
#     iterating through s. referring to each element as "word"
    for word in sentence:
#         for each word, I am adding the length of that word to worth_lengths list
        word_lengths.append(len(word))
#     printing word_lengths for visuals to make sure it's grabbing all the lengths. uncomment line below to see
#         print(word_lengths)
# setting l (the given variable) to the minimum value of the word lengths which would be the shortest word.
    l = min(word_lengths)
    return l # l: shortest word length


'''
Time Complexity of Solutions

def find_short(s):
    sentence = s.split() # this is splitting the string apart based on white spaces into a list format. This scales with the number of words in my stirng. I think O(n)
    word_lengths = [] # this is just setting a variable (word_lengths) to an empty list. this is O(1)
    for word in sentence: # this for loop iterates through my list version of s. this is O(n)
        word_lengths.append(len(word)) # this adds the length of the word. I think this is O(1) because it is just one number it appends.
    l = min(word_lengths) # I think min iterates through my list and finds the lowest value. setting l is O(1) but I think the min function is O(n) because if my list increases, there are more values
    return l # this is just returning one value so this is O(1)

    I think this would be:
    O(n) ; (O1) ; O(n) ; O(1) ; O(1) O(n) ; O(1)
    O(n) ; (O1) ; O(n) ; O(1) ; O(n) ; O(1) -> the O(n) in line 50 overrides O(1) because it's worse
    O(n) ; O(n) ; O(n) ; O(3*1) -> regardless of how many O(1), it is O(1). last thing to do is to determine if the O(n) is nested within another O(n) or if they would just be multiple O(n) that wouldn't cause it to be quadratic
    O(3n) ; O(1) -> I think setting s to s.split() is separate to my for loop. so I think that would be O(2n). I think because my word_lengths list is not nested within the search, the min function would just be another O(n) so just O(3n)
    we take the worst  so O(3n) overrides the O(1)

    Final = O(3n) -> O(n)

'''

'''
Space Complexity of Solutions

def find_short(s):
    sentence = s.split()
    word_lengths = []
    for word in sentence:
        word_lengths.append(len(word))
    l = min(word_lengths)
    return l

    # input = O(n)
    s = string of words -> O(n)

    # aux = O(n)
    sentence = O(n) -> this remains after the function runs
    word_lengths (after for loop) is O(n) but it temporary so not included.

'''