import random

'''
2050 - Parallel Courses III
'''
def generate() -> str:
    tests = []
    min_time = 2
    max_time = 100
    min_nodes = 1
    max_nodes = 50_000
    n = max_nodes
    min_relationships = 0

    # What are edge cases?
    # Obviously, extreme values that lead to TLE
    # but then,
    # maybe one long chain?
    # many parallel chains?

    # one long chain:
    n = 30
    relations = []
    time = [random.randint(min_time, max_time) for _ in range(n)]
    for fro in range(2, n+1):
        to = fro - 1
        relations.append([fro, to])
    test = n.__str__() + "\n" + relations.__str__() + "\n" + time.__str__()
    tests.append(test.__str__().replace(' ', ''))

    # many short chains (skipping every second element)
    n = 30
    relations = []
    time = [random.randint(min_time, max_time) for _ in range(n)]
    for fro in range(2, n+1, 3):
        to = fro - 1
        relations.append([fro, to])
    test = n.__str__() + "\n" + relations.__str__() + "\n" + time.__str__()
    tests.append(test.__str__().replace(' ', ''))

    # many short chains with length 2 (three elements)
    n = 30
    relations = []
    time = [random.randint(min_time, max_time) for _ in range(n)]
    for fro in range(3, n+1, 3):
        to = fro - 1
        relations.append([fro, to])
        relations.append([fro - 1, to - 1])
    test = n.__str__() + "\n" + relations.__str__() + "\n" + time.__str__()
    tests.append(test.__str__().replace(' ', ''))


    for n in [min_nodes, 10, max_nodes]:
        time = [random.randint(min_time, max_time) for _ in range(n)]

        max_relationships = max(int(min(n * (n - 1) / 2, 5 * 10**4)) , 1)
        r = 0
        for relationships in [min_relationships, max_relationships]:
            if n == 1 and relationships > 0:
                continue
            # no relations, vs. many relations
            stop = False
            dag_range = [*range(1, n+1)]
            #random.shuffle(dag_range)
            relations = []
            for i, fro in enumerate(dag_range):
                for to in dag_range[i + 1:]:
                    # This construct prevents cycles because the to is always after the fro
                    # in the array
                    skip = random.randint(0,2)
                    if skip == 1:
                        continue
                    if r > relationships:
                        stop = True
                        break
                    r += 1
                    relations.append([fro, to])
                if stop:
                    break
            test = n.__str__() + "\n" + relations.__str__() + "\n" + time.__str__()
            tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
