"""
File: pythagorean.py
--------------------
Add your comments here.
"""

import math


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    a = input("a: ")
    b = input("b: ")
    a = float(a)
    b = float(b)
    a = a * a
    b = b**2
    c = math.sqrt(a + b)
    print("c = ", c)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
