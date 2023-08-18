import random

def generate() -> str:
    tests = []
    max_num = 100_000

    test = [1,1]
    tests.append(test.__str__())

    test = [1,2]
    tests.append(test.__str__())

    test = [3,2,1]
    tests.append(test.__str__())

    test = [1,2,3]
    tests.append(test.__str__())

    # random cases
    test = [2 * i + 1 for i in range(max_num)]
    tests.append(test.__str__())

    test = [i + 11 for i in range(max_num)]
    tests.append(test.__str__())

    test = [random.randint(1,100) for i in range(max_num)]
    tests.append(test.__str__())

    test = [random.randint(1,100) for i in range(3)] * (max_num // 3)
    tests.append(test.__str__())

    test = []
    for i in range(max_num // 3):
        p = random.randint(1, 20)
        test.extend([p, p+1, p+2])
    tests.append(test.__str__())

    test = []
    for i in range(max_num // 9):
        p = random.randint(1, 40)
        test.extend([p, p, p])
        test.extend([p, p+1, p+2])
        test.extend([p+2, p+2])
    tests.append(test.__str__())

    test = [6,7]
    test.extend([8] * 99_997)
    tests.append(test.__str__())

    return "\n".join(tests)
