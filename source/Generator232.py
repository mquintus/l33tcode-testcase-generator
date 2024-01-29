import random

'''
232 - Implement Queue using Stacks
'''
def generate() -> str:
    tests = []
    min_actions = 1
    max_actions = 100

    min_value = 1
    max_value = 9

    actions = ['push', 'peek', 'pop', 'empty']

    # TC 0
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    for action in ['empty', 'push', 'empty', 'peek', 'push', 'peek', 'pop', 'empty', 'peek', 'pop', 'empty']:
        test_line1.append(action)

        if action == 'push':
            value = random.randint(min_value, max_value)
            while value in existing_values:
                value = random.randint(min_value, max_value)
            existing_values.append(value)
            test_line2.append([value])
            # Do it twice so the second time it fails.
            test_line1.append(action)
            test_line2.append([value])
        elif action == 'pop':
            existing_values.pop(0)
            test_line2.append([])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    n = 100
    # TC 1 - 100 * Random Action out of 3
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    for i in range(n):
        if len(existing_values) == 0:
            action = 'push'
        else:
            action = random.choice(actions)
        test_line1.append(action)

        if action == 'push':
            value = random.randint(min_value, max_value)
            existing_values.append(value)
            test_line2.append([value])
        elif action == 'pop':
            existing_values.pop(0)
            test_line2.append([])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    n = 20
    # TC 2 - Add n items and pop them all randomly
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    offset = random.randint(0, 100)
    for i in range(n):
        if (i == n // 2 or i == n - 2 or i % 5 == 0) and len(existing_values) > 0:
            action = 'peek'
        elif i < n // 2:
            action = 'push'
        else:
            action = 'pop'

        test_line1.append(action)

        if action == 'push':
            value = random.randint(min_value, max_value)
            existing_values.append(value)
            test_line2.append([value])
        elif action == 'pop':
            existing_values.pop(0)
            test_line2.append([])
        else:
            test_line2.append([])

    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    # TC 3 - Add n items and pop them in the same order (FIFO)
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    offset = random.randint(0, 10)
    for i in range(n):
        if i < n // 2:
            action = 'push'
        elif i == n // 2 or i == n - 2:
            action = 'peek'
        else:
            action = 'pop'

        test_line1.append(action)

        if action == 'push':
            value = random.randint(min_value, max_value)
            existing_values.append(value)
            test_line2.append([value])
        elif action == 'pop':
            value = existing_values.pop(0)
            test_line2.append([])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    # TC 4 - Add n items and pop them in the reversed order (LIFO)
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    for i in range(n):
        if i < n // 2:
            action = 'push'
        elif i == n // 2 or i == n - 2:
            action = 'peek'
        elif i == n // 3 or i == n - 3:
            action = 'empty'
        else:
            action = 'pop'

        test_line1.append(action)

        if action == 'push':
            value = max(min_value, (i + offset) % max_value)
            value = max(min_value, min(max_value, value))
            existing_values.append(value)
            test_line2.append([value])
        elif action == 'pop':
            value = existing_values.pop()
            test_line2.append([])
        else:
            test_line2.append([])

    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    # TC 4 - Add n items and pop every one of them but skip every other one
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    for i in range(n):
        if (i == n // 3 or i == (n - 5) or i % 11 == 0):
            action = 'empty'
        elif len(existing_values) > 0 and (i == n // 2 or i == (n - 2) or i % 12 == 0):
            action = 'peek'
        elif len(existing_values) == 0 or i < n // 2:
            action = 'push'
        else:
            action = 'pop'

        test_line1.append(action)

        if action == 'push':
            value = i - offset
            value = max(min_value, min(max_value, value))
            existing_values.append(value)
            test_line2.append([value])
        elif action == 'pop':
            value = existing_values.pop()
            test_line2.append([])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    # TC 5 - Maintain only two items in the set
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    j = random.randint(min_value, max_value)
    for i in range(n):

        if i % 7 == 2:
            action = 'empty'
        elif len(existing_values) == 0:
            action = 'push'
        elif i % 3 == 2:
            action = 'peek'
        else:
            action = 'pop'

        test_line1.append(action)

        if action == 'push':
            value = max(min_value, j % max_value)
            existing_values.append(value)
            test_line2.append([value])
            j += 1
        elif action == 'pop':
            value = existing_values.pop()
            test_line2.append([])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    n = max_actions
    # TC 7 - n * Random Action out of 3
    test_line1 = ['MyQueue']
    test_line2 = [[]]
    existing_values = []
    for i in range(n):
        if len(existing_values) == 0:
            action = 'push'
        else:
            action = random.choice(actions)
        test_line1.append(action)

        if action == 'push':
            value = random.randint(min_value, max_value)
            existing_values.append(value)
            test_line2.append([value])
        elif action == 'pop':
            value = existing_values.pop(0)
            test_line2.append([])
        else:
            test_line2.append([])
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    return '''
'''.join(tests)
