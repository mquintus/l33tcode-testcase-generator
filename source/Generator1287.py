import random

'''
1287 - Element Appearing More Than 25% In Sorted Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4
    minval = 1
    maxval = 10**4 * 2

    for n in [min_num, 3, 5, 100, 100, 100, max_num]:
        test = []
        first_iteration = True
        used_numbers = set()
        some_number = random.randint(minval,maxval)
        while len(test) < n:
            while some_number in used_numbers:
                some_number = random.randint(minval,maxval)
            if first_iteration:
                first_iteration = False
                quarter = (n // 4) + 1
                while quarter < (n / 4):
                    quarter += 1
                if n <= 3:
                    quarter = n
            elif not first_iteration:
                quarter = (n // 4)
                quarter = min(n - len(test), random.randint(1, quarter))
            test += [some_number] * quarter
            used_numbers.add(some_number)
        test.sort()
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
