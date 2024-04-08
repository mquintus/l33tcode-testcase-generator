import random

'''
1700 - Number of Students Unable to Eat Lunch
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100
    minval = 0
    maxval = 1

    for n in [min_num, min_num + 1, min_num + 2, min_num + 3, max_num - 2, max_num - 1, max_num]:
        students = [random.randint(minval, maxval) for _ in range(n)]
        sandwiches = [random.randint(minval, maxval) for _ in range(n)]
        tests.append(students.__str__().replace(' ', ''))
        tests.append(sandwiches.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
