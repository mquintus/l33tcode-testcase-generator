import random

'''
576 - Out of Boundary Paths
'''
def generate() -> str:
    tests = []
    grid_min = 1
    grid_max = 50
    maxMove = 50
    minMove = 0

    # Testcase 1 - Wide grid
    m = 3
    n = grid_max
    moves = maxMove
    startx = random.randint(0, 2)
    starty = n // 2  + random.randint(-10, 10)
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 2 - Thin grid
    m = grid_max
    n = 2
    moves = maxMove
    startx = m // 2
    starty = 1
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 3 - Ball in the center, border barely reachable
    m = random.randint(15, 20)
    n = random.randint(15, 20)
    moves = random.randint(12, 19)
    startx = m // 2
    starty = n // 2
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 4 - Ball in the center, border well reachable
    m = 20
    n = 20
    moves = maxMove
    startx = m // 2 + random.randint(-10, 10)
    starty = n // 2 + random.randint(-10, 10)
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 5 - Border not reachable
    m = 20
    n = 20
    moves = minMove + random.randint(1, 3)
    startx = m // 2 + random.randint(-10, 10)
    starty = n // 2 + random.randint(-10, 10)
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 6 - Border reachable, ball in the center of a vast grid
    m = grid_max
    n = grid_max
    moves = maxMove
    startx = m // 2 + random.randint(-10, 10)
    starty = n // 2 + random.randint(-10, 10)
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 7 - The is only one cell
    m = grid_min
    n = grid_min
    moves = maxMove + random.randint(-10, 0)
    startx = 0
    starty = 0
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    # Testcase 8 - Ball on the bottom right corner
    m = grid_max
    n = grid_max
    moves = maxMove + random.randint(-10, 0)
    startx = m - random.randint(1, 10)
    starty = n - random.randint(1, 10)
    test = [m, n, moves, startx, starty]
    tests.append("\n".join([str(t) for t in test]))

    return '''
'''.join(tests)
