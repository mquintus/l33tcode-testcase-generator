import random

'''
2251 - Number of Flowers in Full Bloom
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 5 * 10**4
    minval = 1
    maxval = 10**9

    test = []
    people = set()
    n = 100
    for i in range(n):
        start = 3 + i % 13
        end = 3 + (start + (i))  % 15
        end = max(start, end)
        test.append([start, end])
        people.add((start + end )// 2)
    people = list(people)
    people.insert(0, 1)
    tests.append(test.__str__().replace(' ', '') + "\n" + people.__str__().replace(' ', ''))

    for n in [min_num, 10, 20, 30, 1000, 10000, max_num - 2]:
        test = []
        people = []
        start = 1
        end = 1
        first = 10**9 + 1
        last = 0
        for _ in range(n):
            keep = random.randint(0,1)
            if keep == 0:
                start = random.randint(minval, maxval)

            first = min(start, first)
            keep = random.randint(0,1)
            if keep == 0:
                end = min(maxval, start + random.randint(0, maxval) // 2)
            end = max(start, end)
            last = max(end, last)
            people.append((start + end )// 2)
            test.append([start, end])
        test.insert(0,[first, first])
        test.insert(0,[last, last])
        people.insert(0, 1)
        people.insert(0, 10**9)
        tests.append(test.__str__().replace(' ', '') + "\n" + people.__str__().replace(' ', ''))

    return '''
'''.join(tests)
