import random

'''
2147 - Number of Ways to Divide a Long Corridor
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    alphabet = 'SP'

    for n in [min_num, 100, 100, max_num]:
        test = [random.choice(alphabet) for _ in range(n)]
        tests.append('"' + "".join(test) + '"')

        test = [random.choice(alphabet)] * n
        tests.append('"' + "".join(test) + '"')

    return '''
'''.join(tests)
