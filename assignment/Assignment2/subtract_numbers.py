"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    fnum = input()
    fnum = float(fnum)
    snum = input()
    snum = float(snum)
    result = float(fnum - snum)
    print(result)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
