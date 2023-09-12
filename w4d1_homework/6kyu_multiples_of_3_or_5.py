'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
'''

'''
Notes/Brainstorm

I can get a number of any size. I need to find all numbers multiple of 3 or 5 and then sum. I think I will need a list to contain all the numbers that are valid. THen I can try summing the numbers from the list.

def func(num):
    nums_mult_3or5 = []
    if num % 3 == 0 or num % 5 == 0:
        nums_mult_3or5.append(num)
    else:
        return 0
    result = 
'''

# link: https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

number = 10

def solution(number):
    # setting an empty container to hold the numbers that are multiples of 3 or 5
    nums_mult_3or5 = []
    # visualization
    print(number)
    # iterating for the numbers through the range of the number given
    for nums in range(number):
        # if it's a multiple of 3 or 5
        if nums % 3 == 0 or nums % 5 == 0:
            # add it to the container
            nums_mult_3or5.append(nums)
            print(nums_mult_3or5)
        # if not a multiple of 3 or 5, add 0.
        else:
            nums_mult_3or5.append(0)
    # setting result variable to equal the sum of the entire list
    result = sum(nums_mult_3or5)
    print(result)
    return result

solution(number)


def solution(number):
    nums_mult_3or5 = []
    for nums in range(number):
        if nums % 3 == 0 or nums % 5 == 0:
            nums_mult_3or5.append(nums)
        else:
            nums_mult_3or5.append(0)
    result = sum(nums_mult_3or5)
    return result

'''
time complexity

def solution(number):
    nums_mult_3or5 = [] -> O(1)
    for nums in range(number):  -> O(n) iterating through all numbers below number
        if nums % 3 == 0 or nums % 5 == 0:  -> O(1) i think because checking 1 number at a time
            nums_mult_3or5.append(nums)  -> O(1) i think because only adding one number
        else:
            nums_mult_3or5.append(0)  -> O(1)
    result = sum(nums_mult_3or5)  -> O(n) I think because it has to iterate through all the numbers that are eligible. This scales based on how big the number is
    return result -> O(1)

    I think overall it's still O(n) because it isn't causing it to iterate through an iteration multiple times
    Final: O(n)
'''

'''
Space complexity

def solution(number):
    nums_mult_3or5 = []
    for nums in range(number):
        if nums % 3 == 0 or nums % 5 == 0:
            nums_mult_3or5.append(nums)
        else:
            nums_mult_3or5.append(0)
    result = sum(nums_mult_3or5)
    return result

    # input space
    O(1) - I think this because it is always just going to be 1 number. There are not multiple inputs.

    # aux space
    I think O(n) because we are iterating through the range of the given number. the result has the sum property as well that sums a list of numbers based around the size of the initial number given.
'''