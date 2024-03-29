"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    cnt = input()
    cnt = int(cnt)
    tmp = cnt
    for i in range(cnt):
        print(tmp)
        tmp = tmp - 1

    print("Liftoff!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
