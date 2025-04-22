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

    # run_test_alternating_brackets()
    # run_test_triangle_same_number_in_each_row()
    # run_test_triangle_all_numbers_in_each_row()


def run_test_alternating_brackets():
    """Tests the    alternating_brackets    function."""
    print()
    print("----------------------------------------------------------")
    print("Testing the   ALTERNATING_BRACKETS   function:")
    print("----------------------------------------------------------")

    print("Test 1 of alternating_brackets: (5, 2)")
    alternating_brackets(5, 2)

    print("Test 2 of alternating_brackets: (3, 1)")
    alternating_brackets(3, 1)

    print("Test 3 of alternating_brackets: (4, 4)")
    alternating_brackets(4, 4)

    print("Test 4 of alternating_brackets: (8, 6)")
    alternating_brackets(8, 6)


def alternating_brackets(m, n):
    """
    Prints alternating left/right square brackets:  m on the first row,
    m-1 on the next row, m-2 on the next, etc, until n on the last row.
    For example, when m = 5 and n = 2:
       [][][
       [][]
       [][
       []
    Precondition:  m and n are positive integers with m >= n.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_triangle_same_number_in_each_row():
    """Tests the    triangle_same_number_in_each_row    function."""
    print()
    print("----------------------------------------------------------")
    print("Testing the   TRIANGLE_SAME_NUMBER_IN_EACH_ROW   function:")
    print("----------------------------------------------------------")

    print("Test 1 of triangle_same_number_in_each_row: (5)")
    triangle_same_number_in_each_row(5)

    print("Test 2 of triangle_same_number_in_each_row: (1)")
    triangle_same_number_in_each_row(1)

    print("Test 3 of triangle_same_number_in_each_row: (3)")
    triangle_same_number_in_each_row(3)

    print("Test 4 of triangle_same_number_in_each_row: (6)")
    triangle_same_number_in_each_row(6)


def triangle_same_number_in_each_row(r):
    """
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 22, the 3rd is 333, etc.
    For example, when r = 5:
       1
       22
       333
       4444
       55555
    Precondition:  r is a non-negative integer.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_triangle_all_numbers_in_each_row():
    """Tests the    triangle_all_numbers_in_each_row    function."""
    print()
    print("----------------------------------------------------------")
    print("Testing the   TRIANGLE_ALL_NUMBERS_IN_EACH_ROW   function:")
    print("----------------------------------------------------------")

    print("Test 1 of triangle_all_numbers_in_each_row: (5)")
    triangle_all_numbers_in_each_row(5)

    print("Test 2 of triangle_all_numbers_in_each_row: (1)")
    triangle_all_numbers_in_each_row(1)

    print("Test 3 of triangle_all_numbers_in_each_row: (3)")
    triangle_all_numbers_in_each_row(3)

    print("Test 4 of triangle_all_numbers_in_each_row: (6)")
    triangle_all_numbers_in_each_row(6)


def triangle_all_numbers_in_each_row(r):
    """
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 12, the 3rd is 123, etc.
    For example, when r = 5:
       1
       12
       123
       1234
       12345
    Precondition:  r is a non-negative integer.
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
