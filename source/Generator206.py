import random

'''
206 - Reverse Linked List
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 100
    minval = -5000
    maxval = 5000

    for n in [min_num, 1, 2, 3, max_num - 3, max_num - 2, max_num - 1, max_num]:
        offset = random.randint(0, (maxval-minval))
        diff = random.randint(-10, 10)
        test = [minval + (offset + i * diff) % (maxval-minval) for i in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
