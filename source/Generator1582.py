from helpers import matrix
import random

'''
1582 - Special Positions in a Binary Matrix
'''
def generate() -> str:
    tests = []
    max_width = 100
    max_height = 100
    max_width_height = 100
    minval = 0
    maxval = 0

    for width in [1, 4, 10, max_width]:
        height = min(max_height, max_width_height // width)
        mymatrix = matrix.get_matrix(height, width, minval, maxval)
        mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 1
        if width > 1 and height > 1:
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 1
        tests.append(mymatrix.__str__().replace(' ', ''))

    maxval = 1
    for width in [2, 50, max_width]:
        height = min(max_height, max_width_height // width)
        mymatrix = matrix.get_matrix(height, width, minval, maxval)
        tests.append(mymatrix.__str__().replace(' ', ''))

    minval = 1
    maxval = 1
    height = 10
    width = 10
    mymatrix = matrix.get_matrix(height, width, minval, maxval)
    for _ in range(10):
        mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
    tests.append(mymatrix.__str__().replace(' ', ''))

    return '''
'''.join(tests)

if __name__ == '__main__':
    print(generate())
