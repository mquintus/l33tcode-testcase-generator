import random

'''
706 - Design HashMap
'''
def generate() -> str:
    tests = []
    min_actions = 1
    max_actions = 4_000 - 2

    min_key = 0
    max_key = 1_000_000

    min_value = 0
    max_value = 1_000_000

    actions = ['put', 'get', 'remove']

    # try only invalid stuff and override values
    test_line1 = ['MyHashMap']
    test_line2 = [[]]
    for i in range(20):
        action = random.choice(actions)
        test_line1.append(action)

        param = [random.randint(min_key, max_key)]
        if action == 'put':
            param.append(random.randint(min_value, max_value))
        test_line2.append(param)
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    # try max values
    test_line1 = ['MyHashMap']
    test_line2 = [[]]
    for i in range(20):
        action = random.choice(actions)
        test_line1.append(action)

        param = [max_key]
        if action == 'put':
            param.append(random.randint(min_value, max_value))
        test_line2.append(param)
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    # minimal (1) actions
    test_line1 = ['MyHashMap', 'get']
    test_line2 = [[], [min_key]]
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    # max out the number of actions
    test_line1 = ['MyHashMap']
    test_line2 = [[]]
    for i in range(max_actions):
        action = random.choice(actions)
        test_line1.append(action)

        param = [max_key]
        if action == 'put':
            param.append(random.randint(min_value, max_value))
        test_line2.append(param)
    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)

    # 1000 * put i, get i, remove i, get i-1 (should have previously been removed)
    test_line1 = ['MyHashMap']
    test_line2 = [[]]
    for i in range(1, max_actions // 4):
        for action in actions:
            test_line1.append(action)
            param = [i]
            if action == 'put':
                param.append(random.randint(min_value, max_actions))
            test_line2.append(param)
        test_line1.append("get")
        param = [i - 1]
        test_line2.append(param)

    test = (test_line1.__str__() + "\n" + test_line2.__str__()).replace("'", '"').replace(" ", "")
    tests.append(test)


    return '''
'''.join(tests)
