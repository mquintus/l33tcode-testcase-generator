import random
import collections 
from functools import reduce
import itertools
'''
2471 - Minimum Number of Operations to Sort a Binary Tree by Level
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**5

    run = 0
    for n in [min_num, 
              min_num+1,
              max_num//2,
              max_num//4*3,
              max_num//5*4,
              max_num-2,
              max_num-1,
              max_num]:
        run += 1
        numbers = [i for i in range(minval, maxval)]
        if run == 3:
            numbers = reduce(lambda x, y: x + y, zip(numbers[1::2][::-1], numbers[0::2]))
        elif run == 4:
            pass  
        elif run == 5:
            numbers = numbers[::-1]
        elif run == 6:
            numbers = numbers[:n//2:-1] + numbers[:n//2]
        elif run == 7:
            numbers = reduce(lambda x, y: x + y, zip(numbers[:n//2:-1], numbers[:n//2]))
        else:
            random.shuffle(numbers)
        test = [numbers[0]]
        numbers = numbers[1:n]
        bfs = collections.deque()
        bfs.append(0)
        currlevelnodes = 1
        nextlevelnodes = 0
        i = 0
        while bfs:
            bfs.popleft()
            if i >= len(numbers):
                break
            left = random.choice([True, True, False])
            right = random.choice([True, True, False])
            if currlevelnodes == 1:
                left_or_right_or_both = random.randint(0,2)
                if left_or_right_or_both == 0:
                    left = True
                    right = False
                elif left_or_right_or_both == 1:
                    left = False
                    right = True
                else:
                    left = True
                    right = True    

            if left:
                test.append(numbers[i])
                i+=1
                if i < len(numbers):
                    bfs.append(i)
                    nextlevelnodes += 1
            else:
                test.append("null")
            
            if i >= len(numbers):
                break
            
            if right:
                test.append(numbers[i])
                i+=1
                if i < len(numbers):
                    bfs.append(i)
                    nextlevelnodes += 1
            else:
                test.append("null")

            currlevelnodes -= 1
            if currlevelnodes == 0:
                #print(currlevelnodes, nextlevelnodes, len(numbers))
                currlevelnodes = nextlevelnodes
                nextlevelnodes = 0
            
        tests.append(test.__str__().replace(' ', '').replace("'", ''))
    
    return '''
'''.join(tests)
