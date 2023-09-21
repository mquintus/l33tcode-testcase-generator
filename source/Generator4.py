import random

'''
4 - Median of Two Sorted Arrays
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 1000
    minval = -1e6
    maxval = 1e6

    m = min_num
    n = 100
    nums1 = sorted([random.randint(minval, maxval) for _ in range(n)])
    nums2 = sorted([random.randint(minval, maxval) for _ in range(m)])
    tests.append((nums1.__str__() + "\n" + nums2.__str__()).replace(' ', ''))

    m = 99
    n = min_num
    nums1 = sorted([random.randint(minval, maxval) for _ in range(n)])
    nums2 = sorted([random.randint(minval, maxval) for _ in range(m)])
    tests.append((nums1.__str__() + "\n" + nums2.__str__()).replace(' ', ''))

    m = max_num // 2
    n = max_num - 1
    nums1 = sorted([random.randint(minval, maxval) for _ in range(n)])
    nums2 = sorted([random.randint(minval, maxval) for _ in range(m)])
    tests.append((nums1.__str__() + "\n" + nums2.__str__()).replace(' ', ''))

    for _ in range(5):
        m = random.randint(1, max_num)
        n = random.randint(1, max_num)
        nums1 = sorted([random.randint(0, 1000) for _ in range(n)])
        nums2 = sorted([random.randint(999, 2000) for _ in range(m)])
        tests.append((nums1.__str__() + "\n" + nums2.__str__()).replace(' ', ''))

    return '''
'''.join(tests)
