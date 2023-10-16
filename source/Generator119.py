import random

'''
119 - Pascal's Triangle II
'''
def generate() -> str:
    tests = []
    minval = 0
    maxval = 33

    for n in [minval, 1, 2, 3, random.randint(4,30), 31, 32, maxval]:
        tests.append(n.__str__())

    return '''
'''.join(tests)
