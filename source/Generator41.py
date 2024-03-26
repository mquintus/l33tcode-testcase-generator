import random

'''
41 - First Missing Positive
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = -10**5
    maxval = 10**5

    # Testcase 1: All numbers are present
    n = 20
    test = [n - i for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 2 - 4: First, second, last, number is missing
    n = 20
    for missing in [0, 1, n-1]:
        test = [n - i for i in range(n)]
        if random.choice([True, False]):
            test[missing] = random.randint(n+1, maxval)
        else:
            test[missing] = random.randint(minval, 0)
        tests.append(test.__str__().replace(' ', ''))

    # Testcase 5: All numbers are double
    n = 20
    test = [int(i//2) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 6: All numbers are tripled
    n = 30
    test = [int(i//3) for i in range(n)]
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 7: Minimal testcase
    test = [min_num]
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 8: Maximal testcase
    n = max_num
    test = [int(i//2) for i in range(2,n)]
    random.shuffle(test)
    tests.append(test.__str__().replace(' ', ''))



    return '''
'''.join(tests)
