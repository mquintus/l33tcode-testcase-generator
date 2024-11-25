import random
import bisect

'''
773 - Sliding Puzzle
'''
def generate() -> str:
    tests = []

    # 1x Solved (0 steps)
    # 4x Possible (1 step, 2 steps, 10 steps, maxsteps-1,maxsteps)
    # 2x Impossible
    def nextSteps(board, zr, zc):
        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr = zr + d[0]
            if nr not in range(max(0, zr-1),min(2, zr+2)): continue
            nc = zc + d[1]
            if nc not in range(max(0, zc-1),min(3, zc+2)): continue
            newboard = [[c for c in row] for row in board]
            newboard[nr][nc],newboard[zr][zc] = newboard[zr][zc],newboard[nr][nc]
            yield newboard

    board = [[1,2,3],[4,5,0]]
    visited = set([tuple([tuple(row) for row in board])])
    states = [(0, board)]
    maxsteps = 0
    i = 0
    while i < len(states):
        steps, state = states[i]
        i += 1
        for r, row in enumerate(state):
            for c, cell in enumerate(row):
                if cell == 0:
                    for nextBoard in nextSteps(state, r, c):
                        #print(nextBoard)
                        if tuple([tuple(row) for row in nextBoard]) not in visited:
                            # Don't visited any generated board twice
                            visited.add(tuple([tuple(row) for row in nextBoard]))
                            states.append([steps+1, nextBoard])
                            if steps > maxsteps:
                                # Remember max difficulty
                                maxsteps = steps
                                #print(maxsteps)
                    continue

    # Generate testcases with increasing difficulty
    for targetsteps in range(maxsteps+2):
        index_left = bisect.bisect_left([state[0] for state in states], targetsteps)
        index_right = bisect.bisect_right([state[0] for state in states], targetsteps)
        index = random.randint(index_left, index_right-1)
        board = states[index][1]
        tests.append(board.__str__().replace(' ',''))

    # Unsolvable testcases are not in `visited`
    for i in range(2):
        nums = list(range(6))
        random.shuffle(nums)
        randomboard = [[nums.pop() for _ in range(3)] for _ in range(2)]
        while tuple([tuple(row) for row in randomboard]) in visited:
            nums = list(range(6))
            random.shuffle(nums)
            randomboard = [[nums.pop() for _ in range(3)] for _ in range(2)]
        tests.append(randomboard.__str__().replace(' ',''))
    
    return '''
'''.join(tests)
