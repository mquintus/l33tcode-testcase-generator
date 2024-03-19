import random

'''
621 - Task Scheduler
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200
    minval = 0
    maxval = 100

    # Testcase 1 - Only one task and the interval is higher than the number of tasks
    n = min_num
    test = []
    for _ in range(n):
        test.extend([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')])
    cooldown = random.randint(1, 10)
    tests.append(test.__str__().replace(' ', '').replace("'", '"') + '\n' + str(cooldown))

    # Testcase 2 - Only one task type and the interval is higher than the number of tasks
    for cooldown in [random.randint(4, 8), maxval]:
        test = []
        test.extend([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')] * max_num)
        tests.append(test.__str__().replace(' ', '').replace("'", '"') + '\n' + str(cooldown))

    # Testcase 3 - Random Frequency for each letter
    for cooldown in [random.randint(4, 8), maxval]:
        freq = {}
        favailable = max_num
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            f = random.randint(1, favailable)
            favailable -= f
            freq[letter] = f
            if favailable == 0:
                break
        test = []
        for letter, f in freq.items():
            test.extend([letter] * f)
        tests.append(test.__str__().replace(' ', '').replace("'", '"') + '\n' + str(cooldown))

    # Testcase 4 - Random Frequency for each letter
    for cooldown in [0, random.randint(4, 8), maxval]:
        freq = {letter: 1 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        favailable = max_num - 26
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            f = random.randint(1, min(10, favailable))
            favailable -= f
            freq[letter] += f
            if favailable == 0:
                break
        test = []
        for letter, f in freq.items():
            test.extend([letter] * f)
        tests.append(test.__str__().replace(' ', '').replace("'", '"') + '\n' + str(cooldown))

    # Testcase 5 - Cooldown is smaller than the number of tasks
    for cooldown in [random.randint(4, 8)]:
        freq = {letter: 10 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        test = []
        for letter, f in freq.items():
            test.extend([letter] * f)
        tests.append(test.__str__().replace(' ', '').replace("'", '"') + '\n' + str(cooldown))

    return '''
'''.join(tests)
