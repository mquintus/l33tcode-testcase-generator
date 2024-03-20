import random

'''
1669 - Merge In Between Linked Lists
'''
def generate() -> str:
    tests = []
    min_num = 3
    #max_num = 100
    max_num = 10**4
    minval = -1000
    maxval = 1000

    for n in [min_num, 10, 21, max_num]:
        for m in [1, max_num]:
            a = random.randint(1, n - 2)
            b = random.randint(a, n - 2)
            list1 = [random.randint(minval, maxval) for _ in range(n)]
            list2 = [random.randint(minval, maxval)*100 for _ in range(m)]
            tests.append(f'{list1.__str__().replace(" ", "")}\n{a.__str__().replace(" ", "")}\n{b.__str__().replace(" ", "")}\n{list2.__str__().replace(" ", "")}')


    return '''
'''.join(tests)
