import random

'''
150 - Evaluate Reverse Polish Notation
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**4 // 2 - 2
    minval = -200
    maxval = 200

    for n in [min_num, 5, 10, 20, 100, 200, 1000, max_num]:
        value = random.randint(minval, maxval)
        test = [str(value)]
        i = 1
        while i < n:
            result = 2147483648
            while result > 2147483647 or result < -2147483648:
                nextval = random.randint(minval, maxval)
                if value == 0 and nextval == 0:
                    operator = random.choice(['+', '-', '*'])
                else:
                    operator = random.choice(['+', '-', '*', '/'])
                nextpos = random.randint(-1, 0)
                if operator == '/':
                    nextpos = 0
                    if value == 0:
                        nextpos = -1

                left,right = value, nextval
                if nextpos == 0:
                    left,right = nextval, value
                if operator == '+':
                    result = left + right
                elif operator == '-':
                    result = left - right
                elif operator == '*':
                    result = left * right
                else:
                    if (left < 0 and right > 0) or (left > 0 and right < 0):
                        result = -((-left) // right)
                    else:
                        result = left // right
            value = result
            #print(left, operator, right, '=', result)
            if nextpos == -1:
                test.append(str(nextval))
            else:
                test.insert(nextpos, str(nextval))
            test.append(operator)
            #print(test)
            i += 1
        tests.append(test.__str__().replace(' ', '').replace("'", '"'))

    return '''
'''.join(tests)
