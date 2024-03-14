import random

'''
930 - Binary Subarrays With Sum
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 30_000
    minval = 0
    maxval = 1

    for n in [min_num, 2,3,4,10,max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        goal = random.randint(0, sum(test))
        tests.append(test.__str__().replace(' ', '') + "\n" + str(goal))

    test = [0] * (max_num // 2 - 1) + [1] + [0] * (max_num // 2 - 1) + [1]
    goal = 0
    tests.append(test.__str__().replace(' ', '') + "\n" + str(goal))

    test = [0] * max_num
    goal = 0
    tests.append(test.__str__().replace(' ', '') + "\n" + str(goal))

    return '''
'''.join(tests)
