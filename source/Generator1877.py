import random

'''
1877 - Minimize Maximum Pair Sum in Array
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    minval = 1
    maxval = 10**5

    for n in [min_num, 10, 20, 100, max_num, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
