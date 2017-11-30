"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathaniel Nordquist.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400, 300, "Two Circles", 'black')

    center_A = rg.Point(200, 150)
    circle_A = rg.Circle(center_A, 50)
    circle_A.fill_color = 'yellow2'
    circle_A.attach_to(window)

    circle_B = rg.Circle(rg.Point(80, 80), 75)
    circle_B.outline_thickness = 3
    circle_B.attach_to(window)

    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(800, 600, 'Circle_and_Rectangle')
    circle = rg.Circle(rg.Point(400, 400), 100)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    corner_1 = rg.Point(200,200)
    corner_2 = rg.Point(500, 400)
    rectangle = rg.Rectangle(corner_1, corner_2)
    center_of_rectangle = rectangle.get_center()
    center_of_rectangle_x = center_of_rectangle.x
    center_of_rectangle_y = center_of_rectangle.y
    rectangle.attach_to(window)

    print('THIS IS THE CIRCLE\'S DATA')
    # \' is the string literal for ' since Python already uses '' to segreate strings. Credit: Python Software
    # Foundation webpage on Python 3.
    print(circle.outline_thickness, '\n', circle.fill_color, '\n', circle.center, '\n', circle.center)
    print('THIS IS THE RECTANGLE\'S DATA')
    print(rectangle.outline_thickness, rectangle.fill_color, center_of_rectangle, center_of_rectangle_x,
          center_of_rectangle_y, sep= '\n')

    window.render()
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE, SUCKA: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    line_1 = rg.Line(rg.Point(50,50), rg.Point(150, 150))
    line_1.attach_to(window)

    endpoint_1 = rg.Point(75, 75)
    endpoint_2 = rg.Point(300, 280)
    line_2 = rg.Line(endpoint_1, endpoint_2)
    # I don't know why I keep trying to get an individual line object, created through a rose graphics function,
    # through the function parameters! You have to ** change the line's instance variables with the dot equals
    # notation.
    line_2.thickness = 5
    line_2.attach_to(window)

    midpoint = line_2.get_midpoint()
    midpoint_x = midpoint.x
    midpoint_y = midpoint.y

    print('LINE\'S DATA')
    print(midpoint, midpoint_x, midpoint_y, sep='\n')
    window.render()
    window.close_on_mouse_click()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
