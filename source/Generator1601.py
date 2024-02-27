import random

def generate():
    tests = ""
    for test in range(8):
        building = 20
        request_count = 16
        requests = []
        for i in range(request_count):
            requests.append(
                [random.randint(0, building - 1), random.randint(0, building - 1)]
            )
        tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

    building = 20
    requests = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [3, 4],
        [4, 3],
        [3, 4],
        [4, 3],
        [3, 4],
        [4, 3],
    ]
    tests += "\n" + "\n".join([building.__str__(), requests.__str__()])

    building = 4
    for orig in range(0, 4):
        for dest in range(0, 4):
            requests.append([orig, dest])
    tests += "\n" + "\n".join([building.__str__(), requests.__str__()])
    return tests
