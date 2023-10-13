from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def move_to_wall(cnt):
    while front_is_clear():
        put_beeper_safe(cnt)
        move()
        cnt = cnt + 1

def check_modulo(cnt):
    tmp = cnt
    while(tmp > 0):
        tmp = tmp - 2
    if(tmp == 1):
        return False
    elif(tmp == 0):
        return True

def cnt_plus(cnt):
    cnt = cnt + 1
def put_beeper_safe(cnt):
    if (check_modulo(cnt) == True):
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()


def move_side_east(cnt):
    if (facing_east() == True):
        turn_left()
        if front_is_clear():
            move()
            turn_left()


def move_side_west(cnt):
    if(facing_west() == True):
        turn_right()
        if front_is_clear():
            move()
            turn_right()


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    cnt = 0
    while(front_is_clear()):
        move_to_wall(cnt)
        move_side_east(cnt)
        move_to_wall(cnt)
        move_side_west(cnt)




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
