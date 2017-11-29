"""
This module lets you practice correcting SYNTAX (notation) errors.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathaniel Nordquist.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.
#DONE: 0. Mark directory as sources root; helps you with autocomplete and 'things like that.'
########################################################################
# Done: 2.
#   Locate the syntax (notation) errors in this file
#   by looking for red underlines.
#
#   For each error, try to make sense of its message.
#     -- Hover or expand as needed -- make sure you see the message!
#
#   Then fix the errors, one by one.
#     -- Fixing one error may bring up additional errors
#          (after a few seconds or when you run or save the module).
#     -- Each time, fix the ERROR that is currently nearest the TOP of the module.
#     -- Often the SOURCE of the error can be on the line just BEFORE
#          the line with a red underline.
#     -- New errors may appear when you RUN the module.
#
#    Finish by RUNNING the corrected program and making sure that it RUNS CORRECTLY.
#    That is, make sure that (per the doc-strings) the program
#    prints some calculated values and makes a Turtle do some things.
#
#  When complete Commit and Push your work (as always).
#
########################################################################

import rosegraphics as rg
import math


def main():
    """ Calls the other functions in this module to demo them. """
    print_math()
    turtle_fun()


def print_math():
    """ Prints some calculated values. """
    # >>This is a function from a different library. Cosine is a function that exists inside the math library.
    # >>Must import via math.function(parameters). Same with pi: math.cos(math.pi). Pi is of course a function.
    x = math.cos(math.pi)
    print(x)

    y = math.sin(math.pi)
    print('The sine of PI is', y)


def turtle_fun():
    """
    Constructs a TurtleWindow,
    constructs a classic SimpleTurtle and asks it to do some things,
    and waits for the user to click anywhere in the window to close it.
    """
    window = rg.TurtleWindow()
# >> Most languagse don't care about indentation, but it is part of Python's code.
    alan = rg.SimpleTurtle()
    alan.pen = rg.Pen('blue', 30)
    alan.paint_bucket = rg.PaintBucket('yellow')

    alan.backward(3 * (47 + 16))
    alan.begin_fill()
    alan.draw_circle(25)
    alan.end_fill()

    alan.forward(200)

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
