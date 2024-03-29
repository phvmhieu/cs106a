"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    NUM_RANDOM, MIN_RANDOM, MAX_RANDOM = map(int, input().split())
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
