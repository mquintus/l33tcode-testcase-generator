import random

'''
525 - Contiguous Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 0
    maxval = 1

    for n in [min_num, 10, 15, 20, max_num-3, max_num-2, max_num-1, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

        #test = [1 for _ in range(n)]
        #tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
