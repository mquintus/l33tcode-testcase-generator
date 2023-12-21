import random
from source.helpers import matrix

'''
1637 - Widest Vertical Area Between Two Points Containing No Points
'''
def generate() -> str:
    tests = []
    min_width = 2
    max_width = 10**5
    minval = 0
    maxval = 10**9

    for height in [min_width, 20, 1000, max_width]:
        for maxval_temp in [7, maxval // height]:
            width = 2
            mymatrix = matrix.get_matrix(height, width, minval, maxval_temp)
            tests.append(mymatrix.__str__().replace(' ', ''))

    return '''
'''.join(tests)
