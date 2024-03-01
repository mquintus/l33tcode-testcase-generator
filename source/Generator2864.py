import random

'''
2864 - Maximum Odd Binary Number
'''
def generate() -> str:
    tests = []

    s = ['1']
    tests.append("".join(s))

    s = [str(random.randint(0,1)) for i in range(100)]
    tests.append("".join(s))

    s = ['1'] + ['0'] * 98 + ['1']
    tests.append("".join(s))

    s = ['1'] * 50 + ['0'] * 50
    tests.append("".join(s))

    s = ['1'] * 50 + ['0'] * 49 + ['1']
    tests.append("".join(s))

    s = ['0'] + ['1'] * 98 + ['0']
    tests.append("".join(s))

    s = ['0', '1'] * 50
    tests.append("".join(s))

    s = ['1', '0'] * 50
    tests.append("".join(s))

    tests = [f'"{test}"' for test in tests]

    return '''
'''.join(tests)
