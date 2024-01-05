import random

'''
300 - Longest Increasing Subsequence
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 2500


    for n in [min_num, 25, 50, 100, 200, 300]:
        maxval = n
        minval = (maxval // 2) - 100
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    minval = -500
    maxval = 500
    n = 250

    offset = random.randint(minval + n, maxval - n)
    test = [offset + i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    offset = random.randint(minval + n, maxval - n)
    test = [offset - i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
