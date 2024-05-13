import random

'''
861 - Score After Flipping Matrix
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 20
    minval = 0
    maxval = 1

    for n in [min_num, 10, max_num]:
        for m in [min_num, 2, 5, max_num]:
            grid = [[random.randint(minval, maxval) for _ in range(n)] for _ in range(m)]
            tests.append(grid.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
