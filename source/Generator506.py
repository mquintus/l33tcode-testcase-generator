import random

'''
506 - Relative Ranks
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4

    for n in [min_num,
              min_num+1,
              min_num+2,
              min_num+3,
              11,
              10**2,
              10**3,
              max_num]:
        mylist=[i*3 for i in range(n)]
        random.shuffle(mylist)
        tests.append(str(mylist).replace(" ", ""))

    
    return '''
'''.join(tests)
