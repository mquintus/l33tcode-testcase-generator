import random

'''
1915 - Number of Wonderful Substrings
'''
def generate() -> str:
    tests = []
    min_num = 1
#   max_num = 7 * 10**3
    max_num = 10**5
    alphabet = 'abcdefhgji'

    for n in [min_num, min_num+1,min_num+2,min_num+3,100,1000,max_num//10,max_num]:
      test = '"' + "".join([random.choice(alphabet) for _ in range(n)]) + '"'
      tests.append(test.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
