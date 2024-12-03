import random

'''
2109 - Adding Spaces to a String
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 3 * 10**5
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for n in [min_num, 10, 200, max_num//10, max_num//5, max_num]:
        number_of_spaces = random.randint(1, n)
        spaces = list(range(0,n))
        random.shuffle(spaces)
        spaces = spaces[:number_of_spaces]
        spaces.sort()
        test = "".join([random.choice(alphabet) for _ in range(n)])
        tests.append('"'+test.__str__()+'"' + "\n" + str(spaces).replace(' ', ''))

    # max out    
    n = max_num
    number_of_spaces = n
    spaces = list(range(0,n))
    test = "".join([random.choice(alphabet) for _ in range(n)])
    tests.append('"'+test.__str__()+'"' + "\n" + str(spaces).replace(' ', ''))
    
    return '''
'''.join(tests)
