import random

'''
380 - Insert Delete GetRandom O(1)
'''
def generate() -> str:
    tests = []
    min_actions = 1
    max_actions = 2 * 10**5

    min_value = -2**31
    max_value = 2**31 - 1

    actions = ['insert', 'remove', 'getRandom']

    # TC 0 - Add 2, get 4 randoms, remove 2
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = set()
    for action in ['insert', 'insert', 'getRandom', 'getRandom', 'getRandom', 'getRandom', 'remove', 'remove']:
        test_line1.append(action)

        if action == 'insert':
            value = random.randint(1, 10)
            while value in existing_values:
                value = random.randint(1, 10)
            existing_values.add(value)
            test_line2.append([value])
            # Do it twice so the second time it fails.
            test_line1.append(action)
            test_line2.append([value])
        elif action == 'remove':
            value = random.choice(list(existing_values))
            existing_values.remove(value)
            test_line2.append([value])
            # Do it twice so the second time it fails.
            test_line1.append(action)
            test_line2.append([value])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    n = 100
    # TC 1 - 100 * Random Action out of 3
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = set()
    offset = random.randint(-n//2, 2*n)
    for i in range(n):
        if len(existing_values) == 0:
            action = 'insert'
        else:
            action = random.choice(actions)
        test_line1.append(action)

        if action == 'insert':
            value = random.randint(offset, offset + n)
            value = max(min_value, min(max_value, value))
            existing_values.add(value)
            test_line2.append([value])

            # Do it twice so the second time it fails.
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = random.choice(list(existing_values))
            existing_values.remove(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    n = 20
    # TC 2 - Add n items and remove them all randomly
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = set()
    offset = random.randint(0, 100)
    for i in range(n):
        if (i == n // 2 or i == n - 2 or i % 5 == 0) and len(existing_values) > 0:
            action = 'getRandom'
        elif i < n // 2:
            action = 'insert'
        else:
            action = 'remove'

        test_line1.append(action)

        if action == 'insert':
            value = i + offset
            value = max(min_value, min(max_value, value))
            existing_values.add(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = random.choice(list(existing_values))
            existing_values.remove(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        else:
            test_line2.append([])

    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    # TC 3 - Add n items and remove them in the same order (FIFO)
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = []
    offset = random.randint(0, 10)
    for i in range(n):
        if i < n // 2:
            action = 'insert'
        elif i == n // 2 or i == n - 2:
            action = 'getRandom'
        else:
            action = 'remove'

        test_line1.append(action)

        if action == 'insert':
            value = i + offset//2
            value = max(min_value, min(max_value, value))
            existing_values.append(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = existing_values.pop(0)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    # TC 4 - Add n items and remove them in the reversed order (LIFO)
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = []
    for i in range(n):
        if i < n // 2:
            action = 'insert'
        elif i == n // 2 or i == n - 2:
            action = 'getRandom'
        else:
            action = 'remove'

        test_line1.append(action)

        if action == 'insert':
            value = i + offset
            value = max(min_value, min(max_value, value))
            existing_values.append(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = existing_values.pop()
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        else:
            test_line2.append([])

    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    # TC 4 - Add n items and remove every one of them but skip every other one
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = []
    for i in range(n):
        if (i == n // 2 or i == (n - 2) or i % 12 == 0) and len(existing_values) > 0:
            action = 'getRandom'
        elif i < n // 2:
            action = 'insert'
        else:
            action = 'remove'

        test_line1.append(action)

        if action == 'insert':
            value = i - offset
            value = max(min_value, min(max_value, value))
            existing_values.append(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = existing_values.pop((i) % len(existing_values))
            test_line2.append([value])
            if random.random() < 0.1:
                # Delete another random number that (probably) doesn't exist.
                test_line1.append(action)
                test_line2.append([random.randint(min_value, max_value)])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    # TC 5 - Maintain only two items in the set
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = []
    j = random.randint(1, 10)
    for i in range(n):
        if i % 3 == 2:
            action = 'getRandom'
        elif len(existing_values) < 2:
            action = 'insert'
        else:
            action = 'remove'

        test_line1.append(action)

        if action == 'insert':
            value = j
            existing_values.append(value)
            test_line2.append([value])
            j += 1
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = existing_values.pop(0)
            test_line2.append([value])
            # Delete another random number that (probably) doesn't exist.
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([random.randint(min_value, max_value)])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    n = 10**5
    # TC 7 - n * Random Action out of 3
    test_line1 = ['RandomizedSet']
    test_line2 = [[]]
    existing_values = set()
    offset = random.randint(-n//2, 2*n)
    for i in range(n):
        if len(existing_values) == 0:
            action = 'insert'
        else:
            action = random.choice(actions)
        test_line1.append(action)

        if action == 'insert':
            value = random.randint(offset, offset + n)
            value = max(min_value, min(max_value, value))
            existing_values.add(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
        elif action == 'remove':
            value = random.choice(list(existing_values))
            existing_values.remove(value)
            test_line2.append([value])
            if random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([value])
            elif random.random() < 0.1:
                test_line1.append(action)
                test_line2.append([random.randint(min_value, max_value)])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    return '''
'''.join(tests)
