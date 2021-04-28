import re

import numpy as np


def check_input_syntactic(input_string):
    """ Validate input string on typos and syntactic errors

    Parameters:
        input_string (str): The input string which is to be checked.

    Returns:
        exit: Exit the program if there are some problems in input string.

    """

    matrix = input_string.split()[0]
    points = " ".join(input_string.split()[1:])

    # check matrix input
    if not bool(re.match('(\d+[х|x]\d+$)', matrix)):
        exit("Invalid matrix input. Please, check and fix it. Example: '5x5 (1, 1) (4, 4)'")

    # check points input
    points_arr = points.split(')')
    for i in range(len(points_arr)):
        if i != len(points_arr) - 1:
            if not bool(re.match('(\s?\(\d+,\s?\d+$)', points_arr[i])):
                exit("Invalid points input. Please, check and fix it. Example: '5x5 (1, 1) (4, 4)'")
        else:
            if not points_arr[i] == '':
                exit("Invalid points input. Please, check and fix it. Example: '5x5 (1, 1) (4, 4)'")


def check_input_logic(matrix, points):
    """
    Check if matrix coordinates are not lower than points coordinates


    Parameters:
        matrix (str): The string with matrix size which is to be checked.

    Returns:
        exit: Exit program if there is a logic error.
    """

    x_coord_matrix, y_coord_matrix = int(matrix.split('x')[0]), int(matrix.split('x')[1])
    x_coords_points, y_coords_points = points[:, 0], points[:, 1]
    if x_coord_matrix < max(x_coords_points) or y_coord_matrix < max(y_coords_points):
        exit("Matrix coordinates are lower than points coordinates. Please, check and fix it.")


def validate_and_parse_input(input_string):
    """
    Validate input string and parse into matrix size and pizza delivery points

    Parameters:
        input_string (str): The string which is to be validated and parsed.

    Returns:
        matrix (str): String with matrix size.
        points (np.array): 2D numpy array with pizza delivery points.
    """

    # check input on syntactic error
    check_input_syntactic(input_string)

    # parse correct input
    matrix = input_string.split()[0]
    points = re.findall(r'(\(.*?,.*?\))', input_string)
    points = np.array(list((eval(point)) for point in points))

    # check input on logic errors
    check_input_logic(matrix, points)

    return matrix, points
