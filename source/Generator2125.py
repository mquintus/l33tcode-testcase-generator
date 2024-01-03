import random

'''
2125 - Number of Laser Beams in a Bank
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 500
    minval = 0
    maxval = 1

    test = []
    n = max_num
    for m in range(min_num):
        test.append("".join([str(random.randint(minval, 7) // 7) for _ in range(n)]))
    tests.append(test.__str__().replace(' ', '').replace("'", '"'))

    test = []
    n = min_num
    for m in range(max_num):
        test.append("".join([str(random.randint(minval, 7) // 7) for _ in range(n)]))
    tests.append(test.__str__().replace(' ', '').replace("'", '"'))


    for n in [100, max_num]:
        test = []
        for m in range(n):
            test.append("".join([str(random.randint(minval, maxval)) for _ in range(n)]))
        tests.append(test.__str__().replace(' ', '').replace("'", '"'))

        test = []
        for m in range(n):
            test.append("".join(["1" for _ in range(n)]))
        tests.append(test.__str__().replace(' ', '').replace("'", '"'))

    test = []
    n = max_num
    for m in range(n):
        test.append("".join([str(random.randint(minval, 1000) // 1000) for _ in range(n)]))
    tests.append(test.__str__().replace(' ', '').replace("'", '"'))

    test = []
    n = max_num
    for m in range(n):
        test.append("".join(["0" for _ in range(n)]))
    tests.append(test.__str__().replace(' ', '').replace("'", '"'))

    return '''
'''.join(tests)
