import random

'''
1326. Minimum Number of Taps to Open to Water a Garden
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 10**4
    minval = 0
    maxval = 100

    # Edge cases:

    ## Alternating 1 and 0
    n = max_num
    tests.append(f"{n}\n" + ([i % 2 for i in range(n+1)]).__str__())

    ## Length is 1
    n = 1
    tests.append(f"{n}\n" + ([1] * (n+1)).__str__())

    ## Testcase 37/38
    n = 97
    tests.append(f"{n}\n" +
        [1,5,3,1,4,5,5,1,2,0,2,2,4,3,0,0,1,4,5,5,0,3,5,1,1,0,0,0,4,1,1,1,0,4,4,1,0,0,2,5,5,4,4,4,2,4,3,4,4,2,3,4,0,2,0,1,0,4,2,3,0,0,0,1,5,2,0,2,4,4,3,3,0,0,3,1,1,1,4,2,5,2,3,1,0,1,0,2,4,3,4,0,2,4,1,1,2,5].__str__())

    ## All is hundred
    n = max_num
    tests.append(f"{n}\n" + ([100] * (n+1)).__str__())

    # General case
    ## All is random
    n = max_num
    tests.append(f"{n}\n" + ([random.randint(0,50) for _ in range(n+1)]).__str__())
    tests.append(f"{n}\n" + ([random.randint(0,10) for _ in range(n+1)]).__str__())
    tests.append(f"{n}\n" + ([random.randint(0,5) for _ in range(n+1)]).__str__())
    tests.append(f"{n}\n" + ([random.randint(0,3) for _ in range(n+1)]).__str__())

    return "\n".join(tests)
