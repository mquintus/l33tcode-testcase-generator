from source.helpers import matrix
import random

'''
2482 - Difference Between Ones and Zeros in Row and Column
'''
def generate() -> str:
    tests = []
    max_width = 100000
    max_height = 100000
    max_width_height = 100000
    minval = 1
    maxval = 1

    for width in [1, 4, int(max_width ** 0.5), max_width]:
        height = min(max_height, max_width_height // width)
        mymatrix = matrix.get_matrix(height, width, minval, maxval)
        mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
        if width > 1 and height > 1:
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
            mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
        tests.append(mymatrix.__str__().replace(' ', ''))

    minval = 0
    maxval = 1
    for width in [int(max_width ** 0.5), max_width // 3, max_width]:
        height = min(max_height, max_width_height // width)
        mymatrix = matrix.get_matrix(height, width, minval, maxval)
        tests.append(mymatrix.__str__().replace(' ', ''))

    minval = 1
    maxval = 1
    height = int(max_width ** 0.5)
    width = int(max_width ** 0.5)
    mymatrix = matrix.get_matrix(height, width, minval, maxval)
    for _ in range(1000):
        mymatrix[random.randint(0, height - 1)][random.randint(0, width - 1)] = 0
    tests.append(mymatrix.__str__().replace(' ', ''))

    return '''
'''.join(tests)

if __name__ == '__main__':
    print(generate())
