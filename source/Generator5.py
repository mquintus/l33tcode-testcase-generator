import random

'''
5 - Longest Palindromic Substring
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000

    alphabet = list('abcdefghijklmnopqrstuvwxzy0123456789')

    test = [random.choice(alphabet) + random.choice(alphabet)]
    tests.append('"' + "".join(test) + '"')

    for n in [min_num, max_num]:
        test = [random.choice(alphabet) for _ in range(n)]
        tests.append('"' + "".join(test) + '"')

        test = [random.choice(alphabet) * 2 for _ in range(max(1, n//2))]
        tests.append('"' + "".join(test) + '"')

    char = random.choice(alphabet)
    test = char * (max_num // 2 - 1) + '65' + random.choice(alphabet) + char * (max_num // 2 - 2)
    tests.append('"' + "".join(test) + '"')

    char = random.choice(alphabet)
    test = char * (max_num // 2) + 'a' + char * (max_num // 2 - 1)
    tests.append('"' + "".join(test) + '"')

    test = [random.choice(alphabet) * (max_num // 5 - random.randint(1,5)) for _ in range(5)]
    tests.append('"' + "".join(test) + '"')

    return '''
'''.join(tests)
