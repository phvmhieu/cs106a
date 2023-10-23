"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""
import math

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    n = input("Enter a number: ")
    n = int(n)
    while(n != 1):
        if(n % 2 == 0):
            tmp = int(n / 2)
            print(n, "is even, so I take half:", tmp)
            n = tmp
        else:
            tmp = int(n * 3 + 1)
            print(n, "is odd, so I make 3n + 1:", tmp)
            n = tmp



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
