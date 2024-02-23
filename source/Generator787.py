import random

'''
787 - Cheapest Flights Within K Stops
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 100

    '''
      TODO analyze testcases and describe a generic formula:
11
[[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
0
2
4
and
13
[[0,2,77],[0,5,43],[0,11,4],[0,12,54],[1,8,91],[2,3,12],[2,5,49],[2,6,67],[2,7,38],[2,11,100],[2,12,38],[3,7,88],[3,9,98],[3,11,76],[3,12,23],[4,0,91],[4,3,54],[4,6,13],[5,3,67],[5,6,34],[5,7,58],[5,8,95],[5,12,8],[6,2,8],[6,3,88],[6,9,53],[6,12,36],[7,0,17],[7,2,68],[7,4,90],[7,6,39],[7,9,94],[7,10,7],[8,4,32],[8,5,80],[8,6,79],[8,7,92],[8,10,61],[9,0,1],[9,4,37],[9,7,62],[9,10,76],[9,12,20],[10,0,60],[10,5,38],[11,0,13],[11,2,52],[11,6,79],[11,7,64],[11,8,50],[11,10,91],[11,12,74],[12,0,26],[12,2,100],[12,4,38],[12,6,78],[12,8,50],[12,10,52]]
10
1
10
'''

    for n in [min_num, min_num + 1, min_num + 2, min_num + 4, min_num + 5, min_num + 11, max_num - 1, max_num]:
        flights = []
        maxflights = min(((n * (n - 1)) // 2), 1000)
        src = n - 1
        dst = 0
        k = random.randint(0, n - 1)
        options = []
        for i in range(n):
            for j in range(n):
                if i != j and random.randint(0, 1) == 1:
                    options.append([i, j, random.randint(1, 10000)])
        random.shuffle(options)
        for i in range(min(len(options), maxflights)):
            flights.append(options[i])
        flights.sort()
        tests.append(n.__str__() + "\n" + flights.__str__().replace(' ', '') + "\n" + src.__str__() + "\n" + dst.__str__() + "\n" + k.__str__())

    return '''
'''.join(tests)
