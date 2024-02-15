import random

'''
2971 - Find Polygon With the Largest Perimeter
'''
def generate() -> str:
    tests = []
    min_num = 3
    max_num = 10**5
    minval = 1
    maxval = 10**9

    for n in [min_num, 40, 500, 10000]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

        test = []
        running = 0
        for _ in range(n):
            test.append(random.randint(minval + running, minval + running + 1))
            running += test[-1]
            if running > maxval:
                break
        print(len(test))
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
