from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def move_backward():
    turn_around()
    safe_pick_up()
    move()

def turn_around():
    turn_left()
    turn_left()

def move_starting():
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()

def move_to_newspaper():
    while left_is_blocked():
        move()
        if(front_is_blocked()):
            turn_right()
    turn_left()
    move()

def safe_pick_up():
    """
    Karel will pick up a beeper on the current corner, if there is one.
    """
    if beepers_present():
        pick_beeper()


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_to_newspaper()
    move_backward()
    move_starting()









# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
