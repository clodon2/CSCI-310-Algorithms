"""
Corey Verkouteren
9/29/24
matrix add function (n^3) recursion
"""

def matrix_add(matrix1, matrix2, output, size):
    """
    add two matrices
    :param matrix1:
    :param matrix2:
    :param output:
    :param size:
    :return:
    """
    if size == 1:
        output[0] = matrix1[0] + matrix2[0]

