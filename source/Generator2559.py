import random

'''
2559 - Count Vowel Strings in Ranges
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
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
