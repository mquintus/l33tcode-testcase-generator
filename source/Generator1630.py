import random

'''
1630 - Arithmetic Subarrays
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 500
    #min_m = 1
    #max_m = 500
    minval = -100
    maxval = 100

    for n in [min_num, max_num]:
        for strategy in ['random', 'sequentially', 'identical']:
            m = n
            if strategy == 'random':
                test = [random.randint(minval, maxval) for _ in range(n)]
            elif strategy == 'sequentially':
                rand = random.randint(2, 100)
                test = [minval + rand*i + random.randint(0,1) for i in range(n)]
            elif strategy == 'identical':
                test = [random.randint(minval, maxval)] * n
            l = []
            r = []
            for i in range(m):
                l.append(random.randint(0, n - 2))
                r.append(random.randint(l[-1] + 1, min(n-1, l[-1] + 2 + i)))
            tests.append(test.__str__().replace(' ', '') + "\n" + l.__str__().replace(' ', '') + "\n" + r.__str__().replace(' ', ''))


    return '''
'''.join(tests)
