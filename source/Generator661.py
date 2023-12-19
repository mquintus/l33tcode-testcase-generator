import random
from source.helpers import matrix

'''
661 - Image Smoother
'''
def generate() -> str:
    tests = []
    max_width = 200
    max_height = 200
    max_width_height = 400
    minval = 0
    maxval = 255

    width = 1
    height = 1
    mymatrix = matrix.get_matrix(height, width, minval, maxval)
    tests.append(mymatrix.__str__().replace(' ', ''))

    for width in [1, 2, 4, 10]:
        height = min(max_height, max_width_height // width)
        mymatrix = matrix.get_matrix(height, width, minval, maxval)
        tests.append(mymatrix.__str__().replace(' ', ''))

    for height in [2, 50, max_height]:
        width = min(max_width, max_width_height // height)
        mymatrix = matrix.get_matrix(height, width, minval, maxval)
        tests.append(mymatrix.__str__().replace(' ', ''))

    return '''
'''.join(tests)

if __name__ == '__main__':
    print(generate())
