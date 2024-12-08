import random

'''
2054 - Two Best Non-Overlapping Events
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 10**5
    minval = 1
    maxval = 10**4

    for n in [min_num, 
              (min_num+max_num)//6, 
              (min_num+max_num)//6*2, 
              (min_num+max_num)//6*3, 
              (min_num+max_num)//6*4, 
              (min_num+max_num)//6*5, 
              max_num]:
        start = [random.randint(minval, maxval) for _ in range(n)]
        duration = [random.randint(minval, maxval//100) for _ in range(n)]
        end = [min(maxval, start[i] + duration[i]) for i in range(n)]
        value = [random.randint(minval, maxval) for _ in range(n)]
        test = [[s,e,v] for s,e,v in zip(start, end, value)]
        tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
