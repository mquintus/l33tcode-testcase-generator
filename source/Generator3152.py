import random

'''
3152 - Special Array II
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 9

    for n in [min_num, 
              (min_num+max_num)//6, 
              (min_num+max_num)//6*2, 
              (min_num+max_num)//6*3, 
              (min_num+max_num)//6*4, 
              (min_num+max_num)//6*5, 
              max_num-10]:
        special = [random.randint(minval, maxval) for _ in range(n//4+1)]
        special.extend([7,8]*(n//4+1))
        special.extend([random.randint(minval, maxval) for _ in range(n//4+1)])
        print(len(special))
        queries = []
        yes_or_no = True
        for _ in range(n+3):
            fr = random.randint(0, len(special)-1)
            yes_or_no = not yes_or_no
            if not yes_or_no:
                to = max(fr, min(len(special)-1, fr + random.randint(0, n+2)))
            elif fr > n//4 and fr < n//4*3:
                to = max(fr, random.randint(fr+1, n//4*3))
            else:
                to = fr+1
                for to in range(fr+1, len(special)-1):
                    if (special[to-1] % 2) == (special[to] % 2):
                        break 
                to -= 1          
            queries.append([fr, to])
        test = special.__str__() + "\n" + queries.__str__()
        tests.append(test.replace(' ', ''))
    
    return '''
'''.join(tests)
