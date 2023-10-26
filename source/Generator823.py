import random

'''
823 - Binary Trees With Factors
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = 2
    maxval = 10**9

    all_numbers = range(minval, maxval)

    test = [i for i in range(2, 1002)]
    tests.append(test.__str__().replace(' ', ''))

    for n in [min_num, 2, 10, 20, max_num // 2, max_num // 2, max_num // 2, max_num]:
        test = set([2,3,4,5,6,7,8,10,12,random.choice(all_numbers)])
        while len(test) < n:
            new_product = max(minval, (random.choice(list(test)) * random.choice(list(test))) % maxval)
            test.add(new_product)
        tests.append(list(test)[:n].__str__().replace(' ', ''))

    return '''
'''.join(tests)
