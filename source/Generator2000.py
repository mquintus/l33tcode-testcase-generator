import random

'''
2000 - Reverse Prefix of Word
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 250
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    subalpha = alphabet[1:]

    k = 'a'
    n = min_num
    test = [random.choice(subalpha) for _ in range(n)]
    tests.append('"'+"".join(test)+'"\n"'+k+'"')
    
    for n in [20, max_num - 2]:
        test = [random.choice(subalpha) for _ in range(n)]
        tests.append('"'+"".join(test)+'"\n"'+k+'"')
        
        test = [random.choice(alphabet) for _ in range(n)]
        test.insert(0,'a')
        tests.append('"'+"".join(test)+'"\n"'+k+'"')

        test = [random.choice(alphabet) for _ in range(n)]
        test.append('a')
        tests.append('"'+"".join(test)+'"\n"'+k+'"')

    n = max_num - 2
    test = [random.choice(subalpha) for _ in range(n)]
    test.append('a')
    tests.append('"'+"".join(test)+'"\n"'+k+'"')
    
    return '''
'''.join(tests)
