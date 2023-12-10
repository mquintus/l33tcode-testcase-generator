import random
from source.helpers.matrix import get_matrix

'''
867 - Transpose Matrix
'''

def generate() -> str:
    tests = []
    maxheight = 10**3
    maxwidth = 10**3
    max_cells = 10**5
    minval = -1000
    maxval = 1000

    width = 1
    height = min(maxheight, max_cells // width)
    matrix = get_matrix(height, width, minval, maxval)
    tests.append(matrix.__str__().replace(' ', ''))

    for height in [1, 2, 3, 10, 20, 50, maxheight - 1]:
        width = min(maxwidth, max_cells // height)
        matrix = get_matrix(height, width, minval, maxval)
        tests.append(matrix.__str__().replace(' ', ''))

    return '''
'''.join(tests)

if __name__ == '__main__':
    print(generate())