import random

'''
85 - Maximal Rectangle
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200
    #max_num = 35
    minval = 0
    maxval = 1

    line = 0
    for num_rows in [min_num+1, max_num-42, max_num]:
        for num_cols in [min_num+1, max_num // 2, max_num]:
            line += 1
            if line == 2 or line == 3:
                continue
            print("line", line )
            matrix = []
            for row in range(num_rows):
                matrix.append([])
                for col in range(num_cols):
                    matrix[-1].append('"' + str(min(maxval, random.randint(minval, 4)))+'"')
            tests.append(matrix.__str__().replace(' ', '').replace("'", ""))

    return '''
'''.join(tests)
