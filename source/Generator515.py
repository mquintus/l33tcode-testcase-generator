import random

'''
515 - Find Largest Value in Each Tree Row
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 10**4
    minval = -100000
    maxval = 100000

    def build_tree(global_counter):
        nodes = []

        while global_counter > 0:
            global_counter -= 1

            nodes.append(random.randint(minval, maxval))

            skip_child = random.randint(1,10)
            if 1 == skip_child:
                nodes.append('null')

        return nodes

    for n in [min_num, 1, 2, 10, 20, 600, 1000, max_num]:
        nodes = build_tree(n)
        tests.append(nodes.__str__().replace(' ', '').replace("'", ""))

    return '''
'''.join(tests)
