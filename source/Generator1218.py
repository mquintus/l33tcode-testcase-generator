import random


def generate() -> str:
    tests = []

    # random
    arr = [random.randint(-1 * 10 ** 4, 1 * 10 ** 4) for i in range(10 ** 5)]
    difference = random.randint(-1 * 10 ** 4, 1 * 10 ** 4)
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    # sequential
    arr = [-1 * 10 ** 4 + i for i in range(2 * 10 ** 4)]
    difference = 5
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    # sequential
    arr = [-1 * 10 ** 4 + i for i in range(2 * 10 ** 4)]
    difference = 10
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    # sequential
    arr = [(1 * 10 ** 4 - 5 * i) % (10 ** 4) for i in range(10 ** 5)]
    difference = -5
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    arr = [1]
    difference = -5
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    arr = [1, 2, 3, 4, 5]
    difference = -1
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    arr = [
        1,
        2,
        3,
        4,
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        4,
        4,
        7,
    ]
    difference = 0
    test = arr.__str__() + "\n" + difference.__str__()
    tests.append(test)

    return "\n".join(tests)
