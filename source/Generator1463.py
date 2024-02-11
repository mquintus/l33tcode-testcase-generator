import random

'''
1463 - Cherry Pickup II
'''
def generate() -> str:
    tests = []
    max_width = 70
    max_height = 70
    max_value = 100
    min_value = 0

    # Testcase 1
    grid = [[random.randint(min_value, max_value) for _ in range(max_width)] for _ in range(max_height)]
    tests.append(grid.__str__().replace(' ', ''))

    # Testcase 2 - Optimal solution is diagonal
    grid = [[0 for _ in range(max_width)] for _ in range(max_height // 2)]
    for i in range(max_height // 2):
        grid[i][i] = random.randint(min_value, max_value)
        grid[i][max_width - 1 - i] = random.randint(min_value, max_value)
    tests.append(grid.__str__().replace(' ', ''))

    # Testcase 3 - Optimal solution is zigzag
    grid = [[0 for _ in range(max_width)] for _ in range(max_height)]
    j = 0
    for i in range(max_height):
        j = (j + 1) % 3
        grid[i][j] = random.randint(min_value, max_value)
        grid[i][max_width - 1 - j] = random.randint(min_value, max_value)
    tests.append(grid.__str__().replace(' ', ''))

    # Testcase 4 - Optimal solution is straight down
    grid = [[0 for _ in range(max_width)] for _ in range(max_height // 2)]
    grid[max_height//2-1][0] = max_value
    grid[max_height//2-1][max_width - 1] = max_value
    for i in range(max_height // 2):
        grid[i][i] = random.randint(1,9)
        grid[i][max_width - 1 - i] = random.randint(1,9)
    tests.append(grid.__str__().replace(' ', ''))

    # Testcase 5 - Narrow grid
    grid = [[random.randint(min_value, max_value) for _ in range(2)] for _ in range(max_height)]
    tests.append(grid.__str__().replace(' ', ''))

    # Testcase 6 - Wide grid
    grid = [[random.randint(min_value, max_value) for _ in range(max_width)] for _ in range(2)]
    tests.append(grid.__str__().replace(' ', ''))

    # Testcase 7 - No points
    grid = [[0 for _ in range(max_width)] for _ in range(max_height)]
    for i in range(max_height):
        for j in range(i+1, max_width - 1 - i):
            grid[i][j] = max_value
    tests.append(grid.__str__().replace(' ', ''))


    return '''
'''.join(tests)
