import random

'''
1235 - Maximum Profit in Job Scheduling
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5*10**4
    minval = 1
    maxval = 10000

    for n in [min_num, 10, 20, 50, 100, 200, 500, max_num]:
        starttime = [random.randint(minval, maxval) for _ in range(n)]
        endtime = [start + random.randint(minval, maxval) for start in starttime]
        profit = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(
            starttime.__str__().replace(' ', '') + "\n" +
            endtime.__str__().replace(' ', '') + "\n" +
            profit.__str__().replace(' ', '')
            )

    return '''
'''.join(tests)
