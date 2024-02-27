import random

'''
543 - Diameter of Binary Tree
'''
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def make_binary_search_tree(arr, skew=2):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return Node(arr[0])
    mid = int(len(arr) // skew)
    root = Node(arr[mid])
    root.left = make_binary_search_tree(arr[:mid], skew)
    root.right = make_binary_search_tree(arr[mid+1:], skew)
    return root

def flatten_binary_search_tree(root):
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
    min_num = 1
    max_num = 10**4
    minval = -100
    maxval = 100

    skew = 100
    for n in [min_num, 10, 20, 30, 100, 1000, max_num]:
        offset = random.randint(minval, maxval)
        test = [minval + ((i + offset) % (maxval - minval)) for i in range(n)]
        skew = max(1.01,skew)
        test = flatten_binary_search_tree(make_binary_search_tree(test, skew))
        skew //= 3
        whole_test = test.__str__().replace(' ', '').replace('None', 'null')
        tests.append(whole_test)

    return '''
'''.join(tests)
