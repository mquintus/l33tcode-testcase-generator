import random

'''
341 - Flatten Nested List Iterator
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 499
    minval = -100
    maxval = 100

    directions = ['deeper', 'deeper', 'return', 'here']


    def create_nested_list(element_count, depth):
        if element_count == 0:
            return [], 0

        myList = []
        while element_count > 0:
            direction = random.choice(directions)
            if direction == 'deeper':
                nestedList, element_count = create_nested_list(element_count - 1, depth + 1)
                myList.append(nestedList)
            elif direction == 'return' and depth > 0:
                break
            elif direction == 'here':
                item = random.randint(minval, maxval)
                myList.append(item)
                element_count -= 1

        return myList, element_count

    for n in [min_num, 10, 20, 30, 50, 100, max_num, max_num]:
        test, element_count = create_nested_list(n, 0)
        tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
