import random

def generate():
    row = 100
    col = 200
    cells = []
    for x in range(col):
        for y in range(row):
            cells.append([y + 1, x + 1])
    random.shuffle(cells)
    tests = "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    row = 10000
    col = 2
    cells = []
    for x in range(col):
        for y in range(row):
            cells.append([y + 1, x + 1])
    random.shuffle(cells)
    tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    row = 2
    col = 10000
    cells = []
    for x in range(col):
        for y in range(row):
            cells.append([y + 1, x + 1])
    random.shuffle(cells)
    tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    row = 200
    col = 100
    cells = []
    for x in range(col):
        for y in range(row):
            cells.append([y + 1, x + 1])
    random.shuffle(cells)
    tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    row = 200
    col = 100
    cells = []
    for x in range(col):
        for y in range(row - 1, -1, -1):
            cells.append([y + 1, x + 1])
    tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    row = 3
    col = 6666
    cells = []
    for x in range(col):
        for y in range(row - 1, -1, -1):
            cells.append([y + 1, x + 1])
    tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])

    row = 2
    col = 10000
    cells = []
    for x in range(col):
        for y in range(row - 1, -1, -1):
            cells.append([y + 1, x + 1])
    tests += "\n" + "\n".join([row.__str__(), col.__str__(), cells.__str__()])
    return tests
