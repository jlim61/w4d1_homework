# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# Introduction:

# Winter is almost here, and you're gearing up for an exciting ski vacation. As a coding enthusiast, you love a good challenge. Here's a fun one for you: let's calculate the number of pairs of gloves you can create from your collection.

# Problem Description:

# You're given an array that describes the color of each glove in your collection. Your task is to write a function that calculates how many pairs of gloves you can form. Remember, a pair consists of two gloves of the same color.

# Function Signature:


# def count_glove_pairs(glove_colors):
#     # Your code here


# Input:

# - `glove_colors` (List of Strings): An array of glove colors. The length of the array (n) will be between 1 and 1000.

# Output:

# - An integer representing the number of pairs you can create from the given gloves.

# Examples:

# Example 1:

# glove_colors = ["red", "green", "red", "blue", "blue"]
# count_glove_pairs(glove_colors)
# Output: 2
# Explanation:You can form 1 pair of red gloves and 1 pair of blue gloves. 2 pairs of gloves.


# Example 2:

# glove_colors = ["red", "red", "red", "red", "red", "red"]
# count_glove_pairs(glove_colors)
# Output: 3
#Explanation: You can form 3 pairs of red gloves.


'''
I am given the job of pairing up gloves. I think I can do this by seeing if the string inside the list of glove colors is the same.
The colors fo the glvoes must be the same if I match them. At the end, I must return the amount of pairs I have. My length of array will be between 1 and 1000.


psudeo
def gloves(glove_list):
    set a pair counter
    iterate over the colors in the glove color list
        while True:
        if they are the same, pair them up and increase pair counter:
            remove the colors that were used from the list, maybe a .pop? or .append
        else:
         pass


def count_glove_pairs(glove_list):
    pair_counter = 0
    for color in range(len(glove_colors)):
        if color in color:
            pair_counter = += 1
        else:
            pass
          
'''

glove_colors = ["red", "red", "red", "red", "red", "red"]
glove_colors2 = ["red", "green", "red", "blue", "blue", "blue"]

# Milad version

# def _count_glove_pairs(glove_colors):
#     colors = {}
#     result = 0
#     for color in glove_colors:
#         if color not in colors:
#             colors[color] = 1
#         elif color in colors:
#             colors[color] += 1
#     for color in colors.values():
#         pair = color//2
#         result += pair
#     return result




# Sean version

# def count_glove_pairs3(glove_colors):
#     color_count = Counter(glove_colors)  # Use Counter to count occurrences
#     pairs = 0
    
#     for count in color_count.values():
#         pairs += count // 2
    
#     return pairs


# print(count_glove_pairs3(glove_colors2))



'''
if using a .count in a for loop, can probably do a hash method
'''
# Dylan version
# def find_pairs(alist):
#     count = 0
#     for color in set(alist):
#         count += alist.count(color) // 2
#     return count

# print(find_pairs(glove_colors))
# print(find_pairs(glove_colors2))

# Dylan version w/ hash map
# def find_pairs(alist):
#     count, hash_map = 0, {}
#     for color in alist:
#         hash_map[color] = hash_map.get(color, 0) + 1
#     for k,v in hash_map.items():
#         count += v // 2
#     return count



# Dylan version w/ hash map 2
def find_pairs(alist):
    count, hash_map = 0, {}
    for color in alist:
        hash_map[color] = hash_map.get(color, 0) + 1
        if hash_map[color] % 2 == 0:
            count += 1
    return count

print(find_pairs(glove_colors))
print(find_pairs(glove_colors2))