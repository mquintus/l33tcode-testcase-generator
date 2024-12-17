import random

'''
2762 - Continuous Subarrays
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**9

    n = 1
    test = [maxval]
    tests.append(test.__str__().replace(' ', ''))

    for n in [min_num,
              max_num//10,
              max_num//5,
              max_num//2,
              max_num//2 + 1,
              max_num - 2,
              max_num - 1]:
        test = [random.randint(minval, 999)]
        for _ in range(n):
            test.append(max(minval, test[-1]+random.randint(-3, 3)))
        tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
