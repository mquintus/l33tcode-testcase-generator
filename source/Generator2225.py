import random

'''
2225 - Find Players With Zero or One Losses
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**5
    minval = 1
    maxval = 10**5

    # Edgecase 1 - Only two matches
    test = []
    a = random.randint(minval, 100)
    b = minval + (a + random.randint(1, 100 - 1)) % maxval
    test.append([b, a])
    test.append([a, b])
    tests.append(test.__str__().replace(' ', ''))

    for n in [10, 100]:
        # Edgecase 2 - All matches are random
        test = set()
        for _ in range(n):
            a = random.randint(minval, maxval)
            b = a
            while b == a:
                b = minval + (a + random.randint(1, maxval - 1)) % maxval
            test.add((a, b))
        test = sorted(list(list(t) for t in test))
        tests.append(test.__str__().replace(' ', ''))

        # Edgecase 3 - Everyone loses once
        all_players = list(range(1, n + 1))
        losers = all_players.copy()
        test = set()
        while losers:
            loser = losers.pop()
            winner = loser
            while winner == loser or (int(winner), int(loser)) in test:
                winner = random.choice(all_players)
            test.add((int(winner), int(loser)))
        test = sorted(list(list(t) for t in test))
        tests.append(test.__str__().replace(' ', ''))

        # Edgecase 4 - Everyone loses twice
        all_players = list(range(1, n // 2 + 1))
        losers = all_players.copy()
        test = set()
        while losers:
            loser = losers.pop()
            for _ in range(2):
                winner = loser
                while winner == loser or (int(winner), int(loser)) in test:
                    winner = random.choice(all_players)
                test.add((int(winner), int(loser)))
        test = sorted(list(list(t) for t in test))
        tests.append(test.__str__().replace(' ', ''))

    # Edgecase 8 - Everyone loses twice
    n = max_num
    start = random.randint(1, max_num // 3)
    end = min(max_num, start + max_num // 2)
    all_players = list(range(start, end))
    losers = all_players.copy()
    test = set()
    while losers:
        loser = losers.pop()
        for _ in range(2):
            winner = loser
            while winner == loser or (int(winner), int(loser)) in test:
                winner = random.choice(all_players)
            test.add((int(winner), int(loser)))
    test = sorted(list(list(t) for t in test))
    tests.append(test.__str__().replace(' ', ''))

    return '''
'''.join(tests)
