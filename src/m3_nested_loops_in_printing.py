"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

import testing_helper
import time


def main():
    """Calls the other functions to test them."""
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_rectangle_of_stars()
    # run_test_triangle_of_stars()
    # run_test_decreasing_exclamation_marks()


def run_test_rectangle_of_stars():
    """Tests the    rectangle_of_stars    function."""
    print()
    print("--------------------------------------------")
    print("Testing the   RECTANGLE_OF_STARS   function:")
    print("--------------------------------------------")

    print("Test 1 of rectangle_of_stars: (3, 5)")
    rectangle_of_stars(3, 5)

    print("Test 2 of rectangle_of_stars: (4, 11)")
    rectangle_of_stars(4, 11)

    print("Test 3 of rectangle_of_stars: (6, 2)")
    rectangle_of_stars(6, 2)


def rectangle_of_stars(r, c):
    """
    Prints a rectangle of stars (asterisks), with r rows and c columns.
    For example, when r = 3 and c = 5:
       *****
       *****
       *****
    Preconditions:  r and c are non-negative integers.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  *** Unless your instructor directs you otherwise,
    #      see the video
    #          nested_loops_in_PRINTING.mp4
    #      in the PREPARATION for this session
    #          ** NOW **
    #      and follow along in that video as you do this problem.
    #      (Pause the video when it completes this problem.)
    #  ***
    #  __
    #  IMPLEMENTATION RESTRICTION:
    #    ** You may NOT use string multiplication **
    #       in this or the other problems in this module, as doing so
    #       would defeat the goal of providing practice at loops within loops.
    # -------------------------------------------------------------------------


def run_test_triangle_of_stars():
    """Tests the    triangle_of_stars    function."""
    print()
    print("-------------------------------------------")
    print("Testing the   TRIANGLE_OF_STARS   function:")
    print("-------------------------------------------")

    print("Test 1 of triangle_of_stars: (5)")
    triangle_of_stars(5)

    print("Test 2 of triangle_of_stars: (1)")
    triangle_of_stars(1)

    print("Test 3 of triangle_of_stars: (3)")
    triangle_of_stars(3)

    print("Test 4 of triangle_of_stars: (6)")
    triangle_of_stars(6)


def triangle_of_stars(r):
    """
    Prints a triangle of stars (asterisks), with r rows.
      -- The first row is 1 star,
         the second is 2 stars,
         the third is 3 stars, and so forth.
    For example, when r = 5:
       *
       **
       ***
       ****
       *****
    Precondition:  r is a non-negative integer.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  *** Unless your instructor directs you otherwise,
    #      see the video
    #          nested_loops_in_PRINTING.mp4
    #      in the PREPARATION for this session
    #          ** NOW **
    #      and follow along in that video as you do this problem.
    #      (Continue the video from where you paused it
    #      in the previous problem.)
    #  ***
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_decreasing_exclamation_marks():
    """Tests the    decreasing_exclamation_marks    function."""
    print()
    print("----------------------------------------------------------")
    print("Testing the   DECREASING_EXCLAMATION_MARKS   function:")
    print("----------------------------------------------------------")

    print("Test 1 of decreasing_exclamation_marks: (5, 2)")
    decreasing_exclamation_marks(5, 2)

    print("Test 2 of decreasing_exclamation_marks: (3, 1)")
    decreasing_exclamation_marks(3, 1)

    print("Test 3 of decreasing_exclamation_marks: (4, 4)")
    decreasing_exclamation_marks(4, 4)

    print("Test 4 of decreasing_exclamation_marks: (8, 6)")
    decreasing_exclamation_marks(8, 6)


def decreasing_exclamation_marks(m, n):
    """
    Prints exclamation marks:  m on the first row,
    m-1 on the next row, m-2 on the next, etc, until n on the last row.
    For example, when m = 5 and n = 2:
       !!!!!
       !!!!
       !!!
       !!
    Precondition:  m and n are positive integers with m >= n.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(
    arguments, expected, test_results, format_string, suffix=""
):
    testing_helper.print_expected_result_of_test(
        arguments, expected, test_results, format_string, suffix
    )


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    testing_helper.print_actual_result_of_test(
        expected, actual, test_results, precision
    )


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The  IF  statement helps prevent   main   from running
# when we are doing special testing within a testing framework.
# The   try .. except   helps prevent error messages on the console
# from being intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise
