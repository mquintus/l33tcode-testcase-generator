import random

'''
950 - Reveal Cards In Increasing Order
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = 1
    maxval = 10**4

    for n in [min_num, min_num + 1, min_num + 2, max_num - 2, max_num - 1, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        test = list(set(test))
        tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
