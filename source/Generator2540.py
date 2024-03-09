import random

'''
2540 - Minimum Common Value
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10000
    minval = 1
    maxval = 10**9 - 1

    # Edgecases:
    # 1. Fewer elements in nums1, match highest number
    # 2. Fewer elements in nums2, match lowest number
    # 3. Fewer elements in nums1, no match
    # 4. Numbers in nums1 and nums2 alternate with duplicates
    # 5. All numbers in nums1 are the same, match highest number of nums2
    # 6. All numbers in nums2 are the same, match highest number of nums1
    # 7. All numbers in nums1 are the same, no match

    # 1, 2, 3. Fewer elements in nums1, match highest number
    for m,n in [(min_num, max_num), (max_num, min_num)]:
        nums1 = sorted([random.randint(100,maxval) for i in range(m)])
        nums2 = sorted([random.randint(1,99) for i in range(n-1)])
        nums1.append(maxval)
        nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    # 3. Numbers in nums1 and nums2 alternate with duplicates
    for match in [True, False]:
        offset = random.randint(10, 20)
        m,n = max_num - 20, max_num - 10
        nums1 = []
        for i in range(m):
            nums1.append(offset + (10*i) + 1)
            nums1.append(offset + (10*i) + 1)
            nums1.append(offset + (10*i) + 3)
        nums2 = []
        for i in range(m):
            nums2.append(offset + (10*i) + 6)
            nums2.append(offset + (10*i) + 7)
            nums2.append(offset + (10*i) + 7)
        if match:
            nums1.append(maxval)
            nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    for match in [True, False]:
        nums1 = [random.randint(1,99)] * (max_num - 2)
        nums2 = [random.randint(1,99)] * (max_num - 2)
        if match:
            nums1.append(maxval)
            nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    for match in [True, False]:
        nums1 = [random.randint(1,99)] * 99999
        nums2 = [random.randint(1,99)] * 99999
        if match:
            nums1.append(maxval)
            nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    return '''
'''.join(tests)
