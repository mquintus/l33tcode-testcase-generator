import random

'''
1026 - Maximum Difference Between Node and Ancestor
'''
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_tree(n, minval, maxval):
    if n == 0:
        return None
    n -= 1
    root = Node(random.randint(minval, maxval))
    left = random.randint(0, n)
    right = n - left
    root.left = create_tree(left, minval, maxval)
    root.right = create_tree(right, minval, maxval)
    return root

def flatten_tree(root):
    if root == None:
        return [None]
    states = [root]
    final_array = [root.val]
    while len(states) > 0:
        new_states = []
        for state in states:
            if state != None:
                new_states.append(state.left)
                new_states.append(state.right)

        i = -1
        for state in new_states:
            i += 1
            if state != None:
                final_array += [state.val]
            else:
                final_array += [None]

        states = new_states
    while final_array[-1] == None:
        final_array.pop()
    return final_array


def generate() -> str:
    tests = []
    min_num = 2
    max_num = 5000
    minval = 1
    maxval = 10**5

    for n in [min_num, 10, 10, 20, 20, 100, 1000, max_num]:
        test = create_tree(n, minval, int(n*(maxval//max_num)))
        whole_test = flatten_tree(test).__str__().replace(' ', '').replace('None', 'null')
        tests.append(whole_test)

    return '''
'''.join(tests)
