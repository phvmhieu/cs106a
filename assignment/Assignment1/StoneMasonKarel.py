from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def move_to_wall():
    while front_is_clear():
        move()

def repair():
    while front_is_clear():
        safe_put()
        move()
    safe_put()


def safe_put():
    if (no_beepers_present()):
        put_beeper()

def move_backward():
    turn_left()
    turn_left()
    move_to_wall()
    turn_left()

def divisible_by_four(n):
    while(n >= 4):
        n = n -4

    if(n == 0):
        return True
    elif(n != 4):
        return False

def final(i):
    if (divisible_by_four(i) == True):
        turn_left()
        repair()
        move_backward()
    if (front_is_clear()):
        move()

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    i = 4
    while front_is_clear():
        final(i)
        i = i + 1
    final(i)
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
