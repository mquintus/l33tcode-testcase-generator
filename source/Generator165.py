import random

'''
165 - Compare Version Numbers
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 500
    separator = "."
    for alphabet in ["000123456789", "01"]:
        alphabetplus = alphabet + separator * 10

        for n1 in [1,50, max_num]:
            for n2 in [1,10, max_num]:
                v1 = random.choice(alphabet)
                nosep = 1
                while len(v1) < n1 - 2:  
                    if nosep < 8:
                        v1 += random.choice(alphabetplus)
                        if v1[-1] != '.':
                            nosep += 1
                    else:
                        v1 += separator
                        nosep = 0
                    v1 += random.choice(alphabet)
                    if v1[-1] != '.':
                       nosep += 1
                    
                v2 = random.choice(alphabet)
                while len(v2) < n2 - 2:  
                    if nosep < 8:
                        v2 += random.choice(alphabetplus)
                        if v2[-1] != '.':
                            nosep += 1
                    else:
                        v2 += separator
                        nosep = 0
                    v2 += random.choice(alphabet)
                    if v2[-1] != '.':
                       nosep += 1
                test = f'"{v1}"\n"{v2}"'
                tests.append(test)
    
    return '''
'''.join(tests)
