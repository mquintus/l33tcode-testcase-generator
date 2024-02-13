import random

'''
2108 - Find First Palindromic String in the Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 100

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    count = 1
    test = []
    for _ in range(count):
        length = 1
        test.append('"' + "".join([random.choice(alphabet) for _ in range(length)]) + '"')
    tests.append(test.__str__().replace(' ', '').replace("'", ''))

    for count in [2, 3, max_num]:
        test = []
        for _ in range(count):
            length = random.randint(minval, maxval)
            test.append('"' + "".join([random.choice(alphabet) for _ in range(length)]) + '"')
        tests.append(test.__str__().replace(' ', '').replace("'", ''))

        test = []
        for _ in range(count):
            length = random.randint(minval, maxval)
            word = [random.choice(alphabet) for _ in range(length)]
            if random.randint(0, 1) == 0:
                word = word[:length//2]
                word = word + word[::-1]
            test.append('"' + "".join(word) + '"')
        tests.append(test.__str__().replace(' ', '').replace("'", ''))

    count = max_num - 1
    test = []
    for _ in range(count):
        length = random.randint(maxval - 10, maxval - 2)
        word = [random.choice(alphabet) for _ in range(length)]
        word = word[:length//2]
        word = word + ["xy"] + word[::-1]
        test.append('"' + "".join(word) + '"')
    length = random.randint(maxval - 10, maxval - 2)
    word = [random.choice(alphabet) for _ in range(length)]
    word = word[:length//2]
    word = word + word[::-1]
    test.append('"' + "".join(word) + '"')
    tests.append(test.__str__().replace(' ', '').replace("'", ''))


    return '''
'''.join(tests)
