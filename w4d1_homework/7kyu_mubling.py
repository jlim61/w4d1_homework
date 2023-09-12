'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

'''
Notes/Brainstorm

What it looks like is that each letter appears the number of items equal to its index.
It takes in a string and, based on the index, repeats that value. It also capitalizes each time and has a dash in between each.
It returns a string so it might be a .join() with them joined by dashes
'''

# link: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(s):
    # making a list version of the string
    list_s = list(s)
    # visualization
    print(list_s)
    # setting index to 0
    i = 0
    # make empty string
    result = ""
    # iterate through each letter in the list
    for letter in list_s:
        # if the letter being looked at IS NOT the last letter in the list, execute code with a dash in between the word
        if i != len(list_s) - 1:
            add_result = letter.lower() * (i + 1)
            i += 1
            result += add_result.capitalize() + "-"
            print(result)
        # if it IS the last letter in the string, only add the letter
        else:
            add_result = letter.lower() * (i + 1)
            i += 1
            result += add_result.capitalize()
            print(result)
    return result

def accum(s):
    list_s = list(s)
    print(list_s)
    i = 0
    result = ""
    for letter in list_s:
        if i != len(list_s) - 1:
            add_result = letter.lower() * (i + 1)
            i += 1
            result += add_result.capitalize() + "-"
            print(result)
        else:
            add_result = letter.lower() * (i + 1)
            i += 1
            result += add_result.capitalize()
            print(result)
    return result


'''
Time complexity

def accum(s):
    list_s = list(s) -> I think list still has to iterate through the string so I think it's O(n)
    print(list_s) -> O(1)
    i = 0 -> O(1)
    result = "" -> O(1)
    for letter in list_s: -> O(n)
        if i != len(list_s) - 1: -> this is a check but only to the index compared to position. however, the list_s can be bigger or smaller so I think O(n)
            add_result = letter.lower() * (i + 1) ->  O(1)
            i += 1 -> O(1)
            result += add_result.capitalize() + "-" ->  O(1)
            print(result) ->  O(1)
        else: ->  O(1)
            add_result = letter.lower() * (i + 1)
            i += 1 ->  O(1)
            result += add_result.capitalize() ->  O(1)
            print(result) ->  O(1)
    return result ->  depending on initial string length, it can be bigger or smaller so I think = O(n)

    I think overall it is O(n). I don't think any of the other O(n) cause it to iterate through itself again
    Final = O(n)
'''

'''
Space complexity

def accum(s):
    list_s = list(s)
    print(list_s)
    i = 0
    result = ""
    for letter in list_s:
        if i != len(list_s) - 1:
            add_result = letter.lower() * (i + 1)
            i += 1
            result += add_result.capitalize() + "-"
            print(result)
        else:
            add_result = letter.lower() * (i + 1)
            i += 1
            result += add_result.capitalize()
            print(result)
    return result

    # input:
    I think input space is O(n) because the value of it can constantly increase or decrease

    # aux:
    s still remains the same and the result will be bigger or smaller depending on how big s is.
    I think s is O(n) and I think result is O(n). 
    I think final is O(n)
'''