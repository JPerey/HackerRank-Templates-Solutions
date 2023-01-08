'''
__intro__

It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  1 to 'n'. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

__Example__

q = [1,2,3,4,5,6,7,8]
If person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,7,8. Only 1 bribe is required. Print '1'.

q = [4,1,2,3]
Person 4 had to bribe 3 people to get to the current position. Print 'Too chaotic'.

__Function Description__

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):

int q[n]: the positions of the people after all bribes

__Returns__

No value is returned. Print the minimum number of bribes necessary or 'Too chaotic' if someone has bribed more than 2 people.

'''

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # copy to your preferred IDE and code there and then copy + paste into HackerRank once solution is found
    bribe_count = 0

    for index, value in enumerate(q):
        abs_distance = abs(value - index)
        if abs_distance > 3:
            print("Too chaotic")
            return
        else:
            if (index - 1) >= 0:
                if (index-1) == 0:
                    for digit in q[0: index]:
                        if digit > value:
                            bribe_count += 1

                else:
                    for digit in q[0: index]:
                        if digit > value:
                            bribe_count += 1
    print(bribe_count)


test_list = [1, 2, 5, 3, 4, 7, 8, 6]  # sample test case 0
response = minimumBribes(test_list)

print(f"response: {response}")


'''

    i = 0
    total_bribe_amount = 0

    def helperMinus(elem, index):  # func to check distance and if anyone bribed someone too much
        abs_distance = abs(elem - (index + 1))
        print(
            f"elem: {elem} || index: {index+1} || abs distance: {abs_distance}")
        if abs_distance > 2:
            return False
        else:
            return True

    def helperBribes(current_elem, values_before_elem):

    for digit in q:
        try:

            chaos_check, bribe_amount = helperMinus(digit, i, q[i+1])
            total_bribe_amount += bribe_amount
            print(
                f"i: {i} || bribe_amount: {bribe_amount} || total_bribe_amount: {total_bribe_amount}")
            print("============")
            if chaos_check:
                i += 1
                pass
            else:
                return "Too Chaotic"
        except:
            pass

    return total_bribe_amount

'''
