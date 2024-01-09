import random

'''
872 - Leaf-Similar Trees
'''
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_list_of_leaves(root, list_of_leaves):
    if root.left is None and root.right is None:
        list_of_leaves.append(root.val)
        return
    if root.left is not None:
        get_list_of_leaves(root.left, list_of_leaves)
    if root.right is not None:
        get_list_of_leaves(root.right, list_of_leaves)

def create_tree(n, minval, maxval, leafnodelist=None):
    if leafnodelist is None and n == 0:
        return None
    if leafnodelist is not None and len(leafnodelist) == 0:
        return None
    if leafnodelist is not None and n <= 1:
        return Node(leafnodelist.pop(0))
    n -= 1
    root = Node(random.randint(1, 100))
    left = random.randint(0, n)
    right = n - left
    if left != 0:
        root.left = create_tree(left, minval, maxval, leafnodelist)
    root.right = create_tree(right, minval, maxval, leafnodelist)
    return root

def flatten_tree(root):
    if root == None:
        return [None]
    states = [root]
    final_array = [root.val]
    #print("Root", root.val)
    while len(states) > 0:
        new_states = []
        for state in states:
            if state != None:
                new_states.append(state.left)
                new_states.append(state.right)

        dir = ['Left', 'Right']
        i = -1
        for state in new_states:
            i += 1
            if state != None:
                #print(dir[i%2] + "child", state.val)
                final_array += [state.val]
            else:
                #print(dir[i%2] + "child", None)
                final_array += [None]

        states = new_states
    while final_array[-1] == None:
        final_array.pop()
    return final_array


def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200
    minval = 1
    maxval = 200

    for n in [min_num, 10, 20, max_num]:
        for equal in [True, False]:
            test1 = create_tree(n, minval, maxval, None)
            list_of_leaves = []
            get_list_of_leaves(test1, list_of_leaves)
            if not equal:
                random.shuffle(list_of_leaves)
                print(list_of_leaves)
                if len(list_of_leaves) == 1:
                    list_of_leaves.append(maxval)
                    n = 3
                    print(list_of_leaves)
            if equal and n == 1:
                n = 2
            test2 = create_tree(n, minval, maxval, list_of_leaves)
            whole_test = flatten_tree(test1).__str__().replace(' ', '').replace('None', 'null') + "\n" + flatten_tree(test2).__str__().replace(' ', '').replace('None', 'null')
            tests.append(whole_test)

    return '''
'''.join(tests)
