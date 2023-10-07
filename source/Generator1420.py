import random

'''
1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**4
    minval = -1000
    maxval = 1000

    n = min_num
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))
    
    n = max_num
    test = [random.randint(minval, maxval) for _ in n]
    tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
