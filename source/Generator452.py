import random

'''
452 - Minimum Number of Arrows to Burst Balloons
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = -2**31
    maxval = 2**31 - 1

    # Testcase 1 - Only one balloon
    n = min_num
    test = []
    for _ in range(n):
        start = random.randint(minval, maxval)
        test.extend([[start, random.randint(start+1, maxval)]])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 2 - 10 balloons, overlapping one by one
    n = 10
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset + i, offset + i + 1])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 3 - 20 balloons, overlapping two by two
    n = 20
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset + i, offset + i + 2])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 4 - 20 balloons, not overlapping
    n = 20
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset + (i * 4), offset + (i * 4) + 2])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 5 - 20 balloons, all overlapping with each getting bigger
    n = 20
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset - (i) - 1, offset + (i) + 1])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 6 - 20 balloons, all overlapping, with each same size
    n = 20
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset + (i), offset + (i) + 100])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 7 - 20 balloons, all overlapping, with each same start point
    n = 20
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset, offset + (i) + 1])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 8 - 20 balloons, all overlapping, with each same end point
    # and then 20 ballons that are not overlapping at all
    n = 20
    test = []
    offset = random.randint(-100, 100)
    for i in range(n):
        test.append([offset - i - 1, offset])
        x = random.randint(minval, max_num)
        test.append([-offset + x, -offset + x + 1])
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 9 - Random numbers
    n = max_num
    test = []
    for _ in range(n):
        start = random.randint(minval, maxval)
        test.extend([[start, random.randint(start, maxval)]])
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
