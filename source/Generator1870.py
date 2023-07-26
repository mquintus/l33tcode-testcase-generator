import random

'''
Asteroid Collision
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**5

    # Edge cases:
    # - only positive values
    # - only negative values
    # - all asteroids explode
    # - 9999 positive and 1 big negative

    # edge case
    dist = [1,1,100000]
    hour_max = 2.01
    tests.append(dist.__str__() + "\n" + hour_max.__str__())

    dist = [1,1,1,100000]
    hour_max = 3.01
    tests.append(dist.__str__() + "\n" + hour_max.__str__())

    # random cases
    for length in [min_num] * 3 + [max_num] * 5:
        hour_max = random.randint(1, 10**9 - 1) + random.randint(0, 99) / 100
        dist = []
        for i in range(0, length):
            a = 0
            while a == 0:
                a = random.randint(minval, maxval)
            dist.append(a)
        tests.append(dist.__str__() + "\n" + hour_max.__str__())

    hour_max = random.randint(1, maxval) + random.randint(0, 99) / 100
    dist = []
    for i in range(1, max_num):
        dist.append(i)
    tests.append(dist.__str__() + "\n" + hour_max.__str__())

    hour_max = random.randint(1, maxval) + random.randint(0, 99) / 100
    dist = []
    for i in range(0, max_num):
        dist.append(max_num - i)
    tests.append(dist.__str__() + "\n" + hour_max.__str__())

    return "\n".join(tests)
