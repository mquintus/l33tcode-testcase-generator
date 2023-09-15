import random

'''
1584. Min Cost to Connect All Points
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = -10**6
    maxval = 10**6

    tests.append(([
        [random.randint(minval, maxval),
        random.randint(minval, maxval)
    ] for _ in range(1)]).__str__())

    tests.append(([
    [
        -((i) % maxval) - 1,
        -((i) % maxval) - 1]
    for i in range(max_num)
    ]).__str__())

    tests.append(([
    [  ((i) % maxval) - 1,
        -((i) % maxval) - 1] for i in range(max_num)
    ]).__str__())

    tests.append(([
        [random.randint(minval, maxval),
        random.randint(minval, maxval)
    ] for _ in range(max_num)]).__str__())

    # draw a circle
    import math
    pi = math.pi

    def PointsInCircum(r,n=1000):
        return [[int(math.cos(2*pi/n*x)*r),int(math.sin(2*pi/n*x)*r)] for x in range(0,n+1)]
    tests.append(PointsInCircum(maxval, max_num - 1)[1:].__str__())


    # Draw lines
    test = []
    for i in range(minval, maxval, maxval // 24):
        for j in range(minval + 1, maxval, maxval // 10):
            test.append([i,j])
    tests.append(test.__str__())

    tests = list(map(lambda test:test.replace(" ", ""), tests))
    return "\n".join(tests)
