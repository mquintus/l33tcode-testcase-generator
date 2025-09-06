import random

'''
2824 - Count Pairs Whose Sum is Less than Target
'''
def generate() -> str:
    tests = []
    min_num = -50
    max_num = 50
    min_len = 1
    max_len = 50

    n = random.randint(min_len, max_len)
    test = [random.randint(min_num, max_num) for _ in range(n)]
    tests.append(test.__str__().replace(' ', ''))
    
    test = random.randint(min_num, max_num)
    tests.append(test.__str__().replace(' ', ''))
    
    return '\n'.join(tests)
