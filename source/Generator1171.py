import random

'''
1171 - Remove Zero Sum Consecutive Nodes from Linked List
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = 1
    maxval = 1000

    # 1. Nodes to be delete are in the beginning
    #
    someval = random.randint(minval, maxval)
    test = [-someval, someval, 4, 5, 6]
    tests.append(test.__str__().replace(" ", ""))

    # 2. Nodes to be delete are in the end
    #
    someval = random.randint(minval, maxval)
    test = [4, 5, 6, someval, -someval,]
    tests.append(test.__str__().replace(" ", ""))

    # 3. Immediate Deletions between non-deletes:
    someval = random.randint(minval, maxval)
    otherval = random.randint(minval, maxval)
    test =[someval, someval, -otherval, otherval, -someval, -someval]
    tests.append(test.__str__().replace(" ", ""))

    # 4. Zero Values
    someval = random.randint(minval, maxval // 30)
    test = []
    for i in range(10):
        test.append(0)
        test.append(someval * i)
        if i == 5:
            test.append(-2 * someval * i)
    tests.append(test.__str__().replace(" ", ""))

    # 5. Negative values first / last
    test = []
    someval = random.randint(minval, maxval // 30)
    for i in range(5):
        test.append(-i * someval)
    for i in range(10):
        test.append(i * someval)
    for i in range(5):
        test.append(-i * someval)
    tests.append(test.__str__().replace(" ", ""))

    # 6. Ambigous answer
    test = [-1, -2, 3, -3]
    tests.append(test.__str__().replace(" ", ""))

    # 7. Long list deleted on last number
    test = [1] * (max_num - 1) + [-1000]
    tests.append(test.__str__().replace(" ", ""))

    # 8. Only one element to delete
    test = [0]
    tests.append(test.__str__().replace(" ", ""))

    return '''
'''.join(tests)
