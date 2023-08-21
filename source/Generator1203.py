import random


def generate() -> str:
    tests = []
    max_length = 20
    for _ in range(2):
        n = max_length
        m = max_length
        group = [random.randint(-1, m - 1) for _ in range(n)]
        beforeItems = []
        for _ in range(n):
            beforeItem = []
            while random.randint(1, 8) < 2:
                beforeItem.append(random.randint(0, n - 1))
            beforeItems.append(beforeItem)
        test = [n.__str__(), m.__str__(), group.__str__(), beforeItems.__str__()]
        tests.append("\n".join(test))

    max_length = 30000
    for _ in range(2):
        n = max_length
        m = max_length
        group = [random.randint(-1, m - 1) for _ in range(n)]
        beforeItems = []
        for _ in range(n):
            beforeItem = []
            while random.randint(1, 8) < 2:
                beforeItem.append(random.randint(0, n - 1))
            beforeItems.append(beforeItem)
        test = [n.__str__(), m.__str__(), group.__str__(), beforeItems.__str__()]
        tests.append("\n".join(test))

    '''
    Add some testcases where all items have dependencies
    '''
    max_length = 40
    n = max_length
    m = max_length
    group = [-1 for _ in range(n)]
    beforeItems = []
    for i in range(0, n):
        beforeItem = []
        if i > 0:
            beforeItem.append(i - 1)
        beforeItems.append(beforeItem)
        if random.randint(1, 8) < 2:
            group[i] = random.randint(-1, m - 1)
    test = [n.__str__(), m.__str__(), group.__str__(), beforeItems.__str__()]
    tests.append("\n".join(test))

    group = [-1 for _ in range(n)]
    beforeItems = []
    for i in range(0, n):
        beforeItem = []
        if i < n - 1:
            beforeItem.append(i + 1)
        beforeItems.append(beforeItem)
        if random.randint(1, 8) < 2:
            group[i] = random.randint(-1, m - 1)
    test = [n.__str__(), m.__str__(), group.__str__(), beforeItems.__str__()]
    tests.append("\n".join(test))

    group = [-1 for _ in range(n)]
    beforeItems = []
    for i in range(0, n):
        beforeItem = []
        if i > 0:
            beforeItem.append(i - 1)
        beforeItems.append(beforeItem)
    test = [n.__str__(), m.__str__(), group.__str__(), beforeItems.__str__()]
    tests.append("\n".join(test))

    group = [-1 for _ in range(n)]
    beforeItems = []
    for i in range(0, n):
        beforeItem = []
        if i < n - 1:
            beforeItem.append(i + 1)
        beforeItems.append(beforeItem)
    test = [n.__str__(), m.__str__(), group.__str__(), beforeItems.__str__()]
    tests.append("\n".join(test))

    return "\n".join(tests)
