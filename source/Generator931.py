import random

'''
931 - Minimum Falling Path Sum
'''
from source.helpers import matrix
def generate() -> str:
    tests = []
    max_width = 100
    minval = -100
    maxval = 100

    width = 1
    height = width
    mymatrix = matrix.get_matrix(height, width, 0, 1)
    tests.append(mymatrix.__str__().replace(' ', ''))

    i = 0
    for width in [2, 3, 50, 60, 70, 80, 90, 95, max_width]:
        height = width
        maxv = maxval
        minv = minval
        if i % 2 == 1:
            minv = 0
            maxv = 1
        mymatrix = matrix.get_matrix(height, width, minv, maxv)
        tests.append(mymatrix.__str__().replace(' ', ''))
        i += 1

    return '''
'''.join(tests)

if __name__ == '__main__':
    print(generate())
