import random

'''
1930 - Unique Length-3 Palindromic Subsequences
'''
def generate() -> str:
    tests = []
    min_num = 3
    max_num = 10**5

    letters = "abcdefghijklmnopqrstuvwxyz"

    for n in [min_num, 100, max_num]: #, max_num]:
        for repeat in [True, False]:
            if repeat:
                test = "".join([random.choice(letters)] * n)
            else:
                test = "".join([random.choice(letters) for _ in range(n)])
            tests.append(f'"{test}"')

    test = 'acab' * (max_num // 4)
    tests.append(f'"{test}"')

    test = 'z' + "".join([random.choice(letters)] * (max_num - 2)) + 'z'
    tests.append(f'"{test}"')

    return '''
'''.join(tests)
