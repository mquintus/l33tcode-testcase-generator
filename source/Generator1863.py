import random

'''
1863 - Sum of All Subset XOR Totals
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 12
    minval = 1
    maxval = 20

    for n in [min_num, 2, 3, 5, 8, 10, 11, max_num]:
       test = [random.randint(minval, maxval) for _ in range(n)]
       tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
