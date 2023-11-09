import random

'''
1759 - Count Number of Homogenous Substrings
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5

    letters = "abcdefghijklmnopqrstuvwxyz"

    n = min_num
    test = "".join([random.choice(letters) for _ in range(n)])
    tests.append(f'"{test}"')

    test = ""
    i = random.randint(0,25)
    for sublength in range(random.randint(15, 25), 100):
        letter = (i + sublength) % 26
        test += letters[letter] * sublength
    tests.append(f'"{test}"')


    for n in [2, 100, 10000]: #, max_num]:
        for repeat in [True, False]:
            if repeat:
                test = "".join([random.choice(letters)] * n)
            else:
                test = "".join([random.choice(letters) for _ in range(n)])
            tests.append(f'"{test}"')

    return '''
'''.join(tests)
