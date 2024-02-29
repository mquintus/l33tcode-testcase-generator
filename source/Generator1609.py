import random

'''
1609 - Even Odd Tree
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

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
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10000

    # Happy case
    odd = 1
    for n in [min_num, 5, 10, 15, 20, 25, 100, 500]:
        parent = None
        original = TreeNode(2 * random.randint(minval, maxval // 4) + odd)
        nodes = [[original, 0]]
        prev_depth = -1
        prev_val = -1
        i = 1
        while i < n:
            parent, depth = nodes.pop(0)
            if depth > prev_depth:
                val = random.randint(minval+(depth+1)**2, maxval-(depth+1)**2)
                if (depth + val) % 2 == odd:
                    val += 1
                prev_depth = depth

            rand = random.randint(0, 4)

            if rand < 4 and i < n:
                i += 1
                left = TreeNode(val)
                parent.left = left
                nodes.append([left, depth+1])
                val += (((odd + depth) % 2) * 2 - 1) * -2
                #if not valid:
                #    val += random.choice([-1, 1])

            if rand >= 1 and i < n:
                i += 1

                right = TreeNode(val)
                parent.right = right
                nodes.append([right, depth+1])
                val += (((odd + depth) % 2) * 2 - 1) * -2
        tests.append(flatten_tree(original).__str__().replace(' ', '').replace('None', 'null'))


    # Sad case
    tests.append('[42]')
    for odd in [0, 1]:
        for direction in [-1, 1]:
            for duplicates in [False, True]:
                if not duplicates and direction == 1 and odd == 1:
                    continue
                for n in [10]:
                    parent = None
                    original = TreeNode(2 * random.randint(minval, maxval // 4) + odd)
                    nodes = [[original, 0]]
                    prev_depth = -1
                    i = 1
                    while i < n:
                        parent, depth = nodes.pop(0)
                        if depth > prev_depth:
                            val = random.randint(minval+(depth+1)**2, maxval-(depth+1)**2)
                            if (depth + val) % 2 == odd:
                                val += 1
                            prev_depth = depth

                        rand = random.randint(0, 4)

                        if rand < 4 and i < n:
                            i += 1
                            left = TreeNode(val)
                            parent.left = left
                            nodes.append([left, depth+1])
                            if not duplicates or random.randint(0, 1):
                                val += (((odd + depth) % 2) * 2 - 1) * -2 * direction
                            #if not valid:
                            #    val += random.choice([-1, 1])

                        if rand >= 1 and i < n:
                            i += 1
                            right = TreeNode(val)
                            parent.right = right
                            nodes.append([right, depth+1])
                            if not duplicates or random.randint(0, 1):
                                val += (((odd + depth) % 2) * 2 - 1) * -2 * direction


                    tests.append(flatten_tree(original).__str__().replace(' ', '').replace('None', 'null'))

    return '''
'''.join(tests)
