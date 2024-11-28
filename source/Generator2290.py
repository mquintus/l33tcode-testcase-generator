import random

'''
2290 - Minimum Obstacle Removal to Reach Corner
'''
def generate() -> str:
    tests = []
    tle = True
    #tle = False
    maxrows = 10**5
    maxcols = 10**5
    minmult = 2
    maxmult = 10**5
    if not tle:
        # Small testcases
        maxrows = 250
        maxcols = 250
        minmult = 2
        maxmult = 250

    for rows in [2, 5, 50, int((maxmult)**.5), maxrows // 50, maxmult // 2]:
        test = []
        cols = max(minmult, maxmult // rows)
        for r in range(rows):
            test.append([])
            for c in range(cols):
                test[-1].append(random.choice([0, 1, 1]))
        test[0][0] = 0
        test[rows - 1][cols - 1] = 0
        tests.append(test.__str__().replace(' ',''))
    
    # Simple maze
    rows = int((maxmult)**.5) // 2
    cols = maxcols // 5
    test = [[1] * cols for _ in range(rows)]
    for r in range(1, rows//2):
        c = max(0, cols - 1 - random.randint(0, 10))
        test[r][c] = 0
    for r in range(rows//2, rows):
        c = min(cols-1,  0 + random.randint(0, 10))
        test[r][c] = 0
    for r in [rows // 5, rows // 5 * 2, rows // 5 * 3, rows // 5 * 4]:
        r = min(rows-1, r + random.randint(0, 10))
        for c in range(1, cols):
            test[r][c] = 0
    test[0][0] = 0
    test[rows - 1][cols - 1] = 0
    tests.append(test.__str__().replace(' ',''))
    
    return '''
'''.join(tests)
