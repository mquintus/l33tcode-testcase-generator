import random

'''
2485 - Find the Pivot Integer
'''
def generate() -> str:
    tests = []
    minval = 1
    maxval = 1000

    for i in range(minval, maxval+1):
        mysum = (i + 1) * i / 2
        pivot = int(mysum ** .5)
        if pivot * pivot == mysum:
            test = str(i+1)
            tests.append(test)
            test = str(i)
            tests.insert(0, test)
            print(i)

    return '''
'''.join(tests[:8]) + "\n"
