"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """

    MIN_RANDOM = 10
    MAX_RANDOM = 99
    cnt = 0
    while(True):
        a = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        b = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        c = a + b
        print("What is ", a, "+", b, "?")
        answer = input("Your answer: ")
        answer = int(answer)
        if(answer == c):
            cnt = cnt + 1
            print("Correct! You've gotten", cnt,  "correct in a row.")
        else:
            print("Incorrect. The expected answer is ", c)
            cnt = 0
        if(cnt == 3):
            break

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
