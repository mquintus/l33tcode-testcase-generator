import random

'''
938 - Range Sum of BST
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
    max_num = 2 * 10**4
    minval = 1
    maxval = 10**5

    for n in [min_num, 100, 200, 900, 1400, 3000, max_num]:
        offset = random.randint(minval, maxval - n)
        test = [i+offset for i in range(n)]
        low = random.randint(offset, offset+n-1)
        high = random.randint(low, offset+n)
        skew = 1.01 + (random.random() * 100)
        #random.shuffle(test)
        test = flatten_binary_search_tree(make_binary_search_tree(test, skew))
        prev_null = True
        #for i in range(len(test)):
        #    if prev_null == False and random.random() < 0.4:
        #        test[i] = None
        #        prev_null = True
        #    else:
        #        prev_null = False
        whole_test = test.__str__().replace(' ', '').replace('None', 'null') + "\n" + low.__str__() + "\n" + high.__str__()
        tests.append(whole_test)

    return '''
'''.join(tests)
