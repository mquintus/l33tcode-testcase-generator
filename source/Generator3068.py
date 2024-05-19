import random

'''
3068 - Find the Maximum Sum of Node Values
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 2 * 10**4
    minval = 0
    maxval = 100

    for n in [min_num, 10, 20, 30, 40, 50, 60, 70, 80]: # 1000, 2000, 3000, max_num]:
        connected = [0]
        allnodes = [i for i in range(1, n)]
        random.shuffle(allnodes)

        values = [random.randint(minval, maxval) for _ in range(n)]
                
        k = random.randint(minval, 2 * maxval)

        edges = []
        for node in allnodes:
            orig = random.choice(connected)
            edges.append([orig, node])
            connected.append(node)

        test = f"{values}\n{k}\n{edges}"
        tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
