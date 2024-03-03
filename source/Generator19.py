import random

'''
19 - Remove Nth Node From End of List
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 30
    minval = 0
    maxval = 100

    for n in [min_num, 2, 3]:
        offset = random.randint(minval + maxval // 2, maxval)
        for delete in range(1, n+1):
            nodes = [offset - i for i in range(n)]
            test = nodes.__str__().replace(' ', '')
            test += f"\n{delete}"
            tests.append(test)

    offset = random.randint(minval + maxval // 2, maxval)
    n = max_num
    for delete in [1, n]:
        nodes = [offset - i for i in range(n)]
        test = nodes.__str__().replace(' ', '')
        test += f"\n{delete}"
        tests.append(test)

    return '''
'''.join(tests)
