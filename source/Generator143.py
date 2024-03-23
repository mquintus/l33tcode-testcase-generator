import random

'''
143 - Reorder List
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5 * 10**4
    minval = 1
    maxval = 1000

    for n in [min_num, min_num + 1, min_num + 2, min_num + 3, min_num + 4, 5000, max_num - 1, max_num]:
        test = [minval + (int(i*1.001) % maxval) for i in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
