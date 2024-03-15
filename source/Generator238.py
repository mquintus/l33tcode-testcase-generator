import random

'''
238 - Product of Array Except Self
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 1000
    minval = -30
    maxval = 30

    nonZeroValues = list(range(minval, 0)) + list(range(1, maxval))

    # Testcase 1 - Only zeros
    test = [0, random.choice(nonZeroValues)]
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 2 - Only minus ones
    test = [-1] * 20
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 3 - Mixed ones and minus ones
    test = [-1] * 20 + [1] * 20
    random.shuffle(test)
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 4 - Random values
    for n in [40, 60, 80, 120, max_num]:
        test = []
        product = 1
        maxint = 2**32-1
        bigvalue = random.choice(nonZeroValues)
        for i in range(max_num):
            product *= abs(bigvalue)
            if product > maxint:
                print('Maxint reached at', i)
                left = max_num - i
                test.extend([-1] * (left // 2))
                test.extend([1] * (left // 2))
                break
            if i % 2 == 0:
                test.append(bigvalue * -1)
            else:
                test.append(bigvalue)
        #random.shuffle(test)
        if n == 60:
            test.insert(0, 0)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
