import random

def generate() -> str:
    tests = []
    max_length = 100_000
    max_num = 10_000
    min_num = -10_000

    test = [7,2,4]
    k = 2
    tests.append(test.__str__() + "\n" + str(k))

    test = [1,1]
    k = 1
    tests.append(test.__str__() + "\n" + str(k))

    test = [1,2]
    k = 1
    tests.append(test.__str__() + "\n" + str(k))

    test = [3,2,1]
    k = 2
    tests.append(test.__str__() + "\n" + str(k))

    test = [1,1,2,2,3,3,4,4,3,3,2,2,1,1,0,0,-1,-1]
    k = 2
    tests.append(test.__str__() + "\n" + str(k))

    test = [random.randint(min_num, max_num) for _ in range(max_length)]
    k = 123

    test = [max_num - (i % (2*max_num)) for i in range(max_length)]
    k = max_length // 3
    tests.append(test.__str__() + "\n" + str(k))

    test = [(i % (2*max_num)) - max_num for i in range(max_length)]
    k = max_length // 3
    tests.append(test.__str__() + "\n" + str(k))

    return "\n".join(tests)
