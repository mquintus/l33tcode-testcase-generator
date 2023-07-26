import random

'''
Asteroid Collision
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 2000
    minval = -10**6
    maxval = 10**6
    # Edge cases:
    # - only positive values
    # - only negative values
    # - all asteroids explode
    # - 9999 positive and 1 big negative
    tests.append(([(i)%1000 + 1  for i in range(max_num)]).__str__())
    tests.append(([-((i) % 1000) - 1 for i in range(max_num)]).__str__())
    tests.append(([1]*(max_num-2) + [-2]).__str__())
    tests.append(([-1]*(max_num-2) + [2]).__str__())
    tests.append(([10,-10]*(max_num//2-1) + [2]).__str__())
    tests.append([-1,1].__str__())
    tests.append([-1,-1].__str__())
    tests.append([-2,1].__str__())
    tests.append([2,-1].__str__())
    tests.append([2,-3].__str__())

    # random cases
    for length in [min_num] * 3 + [max_num] * 5:
        asteroids = []
        for i in range(0, length):
            a = 0
            while a == 0:
                a = random.randint(minval, maxval)
            asteroids.append(a)
        tests.append(asteroids.__str__())

    return "\n".join(tests)
