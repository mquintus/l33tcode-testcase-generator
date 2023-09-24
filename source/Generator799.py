import random

'''
799 - Champagne Tower
'''
def generate() -> str:
    tests = []

    pouring = int(1e9)
    row = 99
    col = 99
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    pouring = int(1e9)
    row = 99
    col = 78
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    pouring = int(1e9)
    row = 99
    col = random.randint(40,60)
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    pouring = int(1e9)
    row = 0
    col = 0
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    pouring = 0
    row = 0
    col = 0
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    pouring = 1
    row = 0
    col = 0
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    pouring = 8
    row = 3
    col = 3
    test = pouring.__str__() + "\n" + row.__str__() + "\n" + col.__str__()
    tests.append(test)

    return '''
'''.join(tests)
