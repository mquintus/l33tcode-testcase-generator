from .helpers import helpers

'''
2265 - Count Nodes Equal to Average of Subtree
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    minval = 0
    maxval = 1000

    for n in [min_num, 2, 12, 13, max_num, max_num, max_num, max_num]:
        test = helpers.binary_tree_with_duplicates(n, minval, maxval)
        tests.append(test.__str__().replace(' ', '').replace('None', 'null'))

    return '''
'''.join(tests)
