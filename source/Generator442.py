import random

'''
442 - Find All Duplicates in an Array
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5

    # Testcase 1 - Only unique elements
    test = [i for i in range(1, 11)]
    random.shuffle(test)
    tests.append(test.__str__().replace(' ', ''))

    # Testcase 2 - Only doubled elements
    offset = random.randint(2, 6)
    test = [(i//2)+offset for i in range(0, 12)]
    random.shuffle(test)
    tests.append(test.__str__().replace(' ', ''))

    lengths = [min_num, 10, 21, max_num - 42, max_num - 100, max_num]
    #lengths = [min_num, 10, 21, 42, 100, 8000]

    for n in lengths:
        skipped = 0
        used = 0
        test = []
        for i in range(1,n+1):
            #print("n: ", n, "i: ", i, "used: ", used, "skipped: ", skipped, "remaining: ", n - i - skipped)
            remaining = n - i - skipped
            if used < n and (remaining <= 0 or random.randint(0, 2) <= 1):
                test.append(i)
                used += 1

                remaining = (n - i) - skipped
                if used < n and (remaining <= 0 or random.randint(0, 4) == 0):
                    used += 1
                    test.append(i)
                    skipped -= 1
            else:
                skipped += 1
            #print("n: ", n, "i: ", i, "used: ", used, "skipped: ", skipped, "remaining: ", n - i - skipped)
        tests.append(test[::-1].__str__().replace(' ', ''))

    return '''
'''.join(tests)
