import random

'''
1792 - Maximum Average Pass Ratio
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**5

    for n in [min_num, 
              min_num+1,
              max_num//2,
              max_num//4*3,
              max_num-1,
              max_num]:
        r = random.randint(1,10)
        p = [random.randint(minval, maxval) for _ in range(n)]
        f = [random.randint(minval, maxval)//r for _ in range(n)]
        t = [min(maxval, p+f) for p, f in zip(p, f)]
        e = random.randint(minval, maxval)
        test = [[p,t] for p, t in zip(p, t)]
        tests.append(test.__str__().replace(' ', '')+'\n'+str(e))

    p = [random.randint(minval, maxval) for _ in range(n)]
    f = [0 for _ in range(n)]
    t = [min(maxval, p+f) for p, f in zip(p, f)]
    e = random.randint(minval, maxval)
    test = [[p,t] for p, t in zip(p, t)]
    tests.append(test.__str__().replace(' ', '')+'\n'+str(e))

    p = [1 for _ in range(n)]
    f = [random.randint(minval, maxval) for _ in range(n)]
    t = [min(maxval, p+f) for p, f in zip(p, f)]
    e = random.randint(minval, maxval)
    test = [[p,t] for p, t in zip(p, t)]
    tests.append(test.__str__().replace(' ', '')+'\n'+str(e))

    return '''
'''.join(tests)
