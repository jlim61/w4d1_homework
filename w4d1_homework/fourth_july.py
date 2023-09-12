'''
4th of July Time Complexity!
A city is putting on a fireworks show for the 4th of July. There are `n` types of fireworks, and for each type, there’s a specific amount of time it takes to launch that firework.

The city wants to put on a show that lasts for `m` minutes.The function `create_show` takes a list of fireworks (each represented as an integer indicating the time in minutes it takes to launch) and a total time for the show `m`.

 The function will return a list of fireworks that will fill the show’s time as evenly as possible.

Here’s the Python function:

'''


'''import random

def create_show(fireworks, show_time):
    fireworks.sort()

    show = []

    remaining_time = show_time


    while remaining_time > 0 and fireworks:

           # Select a random firework

           firework = random.choice(fireworks)


           if firework <= remaining_time:

               # Add the firework to the show

               show.append(firework)

               remaining_time -= firework

          else:

              # This firework is too long, remove it from consideration

              fireworks.remove(firework)

  return show

'''

'''
time complexity

import random

def create_show(fireworks, show_time):
    fireworks.sort() -> O(n) i think because it has to go through the list and sort them based on the value of each element

    show = [] -> O(1)

    remaining_time = show_time -> O(1)


    while remaining_time > 0 and fireworks: -> O(n) I think because the check is based on fireworks and that means it has to check its values. the number of types of fireworks can be bigger or smaller

           # Select a random firework

           firework = random.choice(fireworks) -> O(1) i think because it's just setting a variable to one element


           if firework <= remaining_time:  -> O(1)

               # Add the firework to the show

               show.append(firework) -> O(1)

               remaining_time -= firework -> O(1)

          else:

              # This firework is too long, remove it from consideration

              fireworks.remove(firework) -> O(1) i think because it's comparing the specific 1 firework to a single number.

  return show

  final: O(log n) I think it's O log n because the number of time is decreasing over time. I'm not sure which line is the O lon n though.
'''


'''
space complexity

# input space
O(n) I think because it has a fixed time and it has a number of types of fireworks BUT the types of fireworks can be any size.

# aux space
O(n) I think because the number of elements of the show would be based on how much time there is and how many fireworks they can squeeze into that allotted time.
'''