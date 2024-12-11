import random

'''
2779 - Maximum Beauty of an Array After Applying Operation
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 0
    maxval = 10**5

    for n in [min_num,
                (min_num+max_num)//6,
                (min_num+max_num)//6*2,
                (min_num+max_num)//6*3,
                (min_num+max_num)//6*4,
                (min_num+max_num)//6*5,
                max_num
              ]:
        test = [random.randint(minval, maxval) for _ in range(n)]
        k = random.randint(1, maxval)
        tests.append(test.__str__().replace(' ', '')+"\n"+str(k))
    
    n = max_num
    k = 0
    test = [random.randint(minval, maxval) for _ in range(n)]
    tests.append(test.__str__().replace(' ', '')+"\n"+str(k))
    
    return '''
'''.join(tests)
