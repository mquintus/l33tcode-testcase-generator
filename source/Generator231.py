import random

'''
231 - Power of Two
'''
def generate() -> str:
    tests = []
    min_num = 0
    max_num = 30

    # Testcase 1: Zero
    n = 0 
    tests.append(n.__str__())

    # Testcase 2: Some true number
    n = 2 ** random.randint(min_num, max_num)
    tests.append(n.__str__())
    
    # Testcase 3: Negative
    n = -1 * n 
    tests.append(n.__str__())
    
    # Testcase 4: Big number, result true
    n = (2 ** random.randint(max_num - 6, max_num))
    tests.append(n.__str__())
    
    # Testcase 5: Big number, result true
    n = (2 ** random.randint(max_num - 12, max_num - 7))
    tests.append(n.__str__())
    
    # Testcase 6: Sum of two valid numbers
    n = (2 ** random.randint(max_num - 6, max_num - 1))
    n += (2 ** random.randint(min_num, max_num - 7))
    tests.append(n.__str__())
    
    # Testcase 7: Sum of three valid numbers
    n += 2 ** max_num
    tests.append(n.__str__())
    
    # Testcase 8: Valid number minus 1
    n = (2 ** random.randint(max_num - 6, max_num))
    n -= 1
    tests.append(n.__str__())
    

    return '''
'''.join(tests)
