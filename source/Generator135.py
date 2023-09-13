import random

# 135 - Candy

def generate() -> str:
    tests = []
    max_length = 20_000
    max_num = 20_000
    min_num = 0

    test = [7,2,4]
    tests.append(test.__str__())

    test = [1,1]
    tests.append(test.__str__())

    test = [100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]
    tests.append(test.__str__())

    test = [6,7,6,5,4,3,2,1,0,0,0,1,0]
    tests.append(test.__str__())

    test = [random.randint(min_num, max_num) for _ in range(max_length)]
    tests.append(test.__str__())

    test = [random.randint(min_num, max_num) for _ in range(max_length)]
    tests.append(test.__str__())

    test = [int(max_num - ((max_num - (i // 2)) % (max_num // 5))) for i in range(max_length)]
    tests.append(test.__str__())

    test = [i % int(max_num // 5) for i in range(max_length)]
    tests.append(test.__str__())


    return "\n".join(tests)
