import random

'''
141 - Middle of the Linked List
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 100

    for n in [*range(min_num, 4), max_num-1, max_num]:
        test = [i for i in range(maxval, max(maxval-n, minval-1), -1)]
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
