import random

'''
1921 - Eliminate Maximum Number of Monsters
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 100_000
    min_dist = 1
    #max_dist = 10000
    min_speed = 1
    max_speed = 10

    for n in [min_num, 2, 100, 100, 100, 100, max_num, max_num]:
        max_dist = min(100_000, max_speed * (2*n//3))
        dist = [random.randint(min_dist, max_dist) for _ in range(n)]
        speed = [random.randint(min_speed, max_speed) for _ in range(n)]
        tests.append(f"{dist}\n{speed}".replace(' ', ''))

    return '''
'''.join(tests)
