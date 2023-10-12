import random

'''
1095 - Find in Mountain Array
'''
def generate() -> str:
    tests = []
    min_num = 3
    max_num = 10**4
    minval = 0
    maxval = 10**9
    height = -1

    for n in [min_num, 10, 100, 200, 500, 1000, max_num]:
        peak = random.randint(1, n - 2)
        mountain = []
        maxdiff = 10
        if n == 200:
            maxdiff = random.randint(1000, 10000)
        for i in range(n):
            diff = random.randint(1, maxdiff)
            if i <= peak:
                height += diff
                if height >= maxval:
                    height = maxval
                    peak = i
            else:
                height -= diff
                height = max(minval, height)
            mountain.append(height)
            if i > peak and height == minval:
                break
        target = random.choice(mountain)
        tests.append(mountain.__str__().replace(' ', '') + "\n" + target.__str__())

    return '''
'''.join(tests)
