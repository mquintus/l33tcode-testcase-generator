import random

'''
2610 - Convert an Array Into a 2D Array With Conditions
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200

    for n in [min_num, 10, 10, 20, 30, 40, 50, max_num]:
        test = [random.randint(1, n) for _ in range(n)]
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
