import random

def get_matrix(height, width, minval, maxval):
    matrix = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(random.randint(minval, maxval))
        matrix.append(row)
    return matrix

