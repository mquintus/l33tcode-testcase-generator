import random

'''
349 - Intersection of Two Arrays
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 1
    maxval = 100

    # Edgecases:
    # 1. Fewer elements in nums1, match highest number
    # 2. Fewer elements in nums2, match lowest number
    # 3. Fewer elements in nums1, no match
    # 4. Numbers in nums1 and nums2 alternate with duplicates
    # 5. All numbers in nums1 are the same, match highest number of nums2
    # 6. All numbers in nums2 are the same, match highest number of nums1
    # 7. All numbers in nums1 are the same, no match

    # 1, 2, Fewer elements in nums1, match highest number
    for m,n in [(min_num, max_num), (max_num, min_num)]:
        nums1 = sorted([random.randint(50,maxval) for i in range(m-1)])
        nums2 = sorted([random.randint(minval,50) for i in range(n-1)])
        nums1.append(maxval)
        nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    # 3. Numbers in nums1 and nums2 alternate with duplicates
    for match in [True, False]:
        offset = random.randint(10, 20)
        m,n = max_num // 13, max_num // 12
        nums1 = []
        for i in range(m):
            nums1.append(offset + (10*i) + 1)
            nums1.append(offset + (10*i) + 1)
            nums1.append(offset + (10*i) + 3)
        nums2 = []
        for i in range(n):
            if match:
                nums2.append(offset + (10*i) + 1)
            nums2.append(offset + (10*i) + 6)
            nums2.append(offset + (10*i) + 7)
        if match:
            nums1.append(maxval)
            nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    for match in [True, False]:
        nums1 = [random.randint(1,99)] * (max_num - 5)
        nums2 = [random.randint(1,99)] * (max_num - 5)
        if match:
            nums1.append(maxval)
            nums1.append(maxval)
            nums2.append(maxval)
            nums2.append(maxval)
        test = f"{nums1}\n{nums2}".replace(" ", "")
        tests.append(test)

    max_num = 1000

    nums1 = [random.randint(100,299) for i in range(max_num - 1)]
    nums2 = []
    for i in range(0, len(nums1), 2):
        nums2.append(nums1[i])
        nums2.append(random.randint(300,500))
    test = f"{nums1}\n{nums2}".replace(" ", "")
    tests.append(test)

    nums1 = []
    nums2 = []
    for i in range(0, max_num):
        nums1.append(i)
        nums2.append(max_num - i)
    test = f"{nums1}\n{nums2}".replace(" ", "")
    tests.append(test)


    return '''
'''.join(tests)
