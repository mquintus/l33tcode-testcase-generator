import random

'''
857 - Minimum Cost to Hire K Workers
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4
    
    n = min_num
    k = 1
    quality = [random.randint(1, n) for _ in range(n)]
    wages   = [random.randint(1, n) for _ in range(n)]
    test = f"{quality}\n{wages}\n{k}"
    tests.append(test.replace(' ', ''))

    for n in [100, max_num]:
        for k in [3, n//3, 2*(n//3)]: 
            quality = [random.randint(1, n) for _ in range(n)]
            wages   = [random.randint(1, n) for _ in range(n)]
            test = f"{quality}\n{wages}\n{k}"
            tests.append(test.replace(' ', ''))
    return '''
'''.join(tests)
