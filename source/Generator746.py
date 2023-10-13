import random

'''
746 - Min Cost Climbing Stairs
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 1000
    minval = 0
    maxval = 999

    for n in [min_num, min_num+1, 30, 42, 51, max_num - 1, max_num]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    test = [random.randint(0, 1) for _ in range(max_num)]
    tests.append(test.__str__().replace(' ', ''))


    return '''
'''.join(tests)
