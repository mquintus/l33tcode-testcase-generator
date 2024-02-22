import random

'''
997 - Find the Town Judge
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 1000
    max_relations = 9999

    for n in [1, 2, 3, 4, 5, 6, max_num - 1, max_num]:
        judge = random.randint(1, n)
        if n % 2 == 1:
            judge = 0
        trust = []
        relations = 0
        abort = False
        #print(judge)
        if judge != 0:
            for i in range(1,n+1):
                if i == judge:
                    continue
                relations += 1
                trust.append([i,judge])

        for i in range(1,n+1):
            for j in range(1,n+1):
                if i != j and (j != judge and (i != judge and random.randint(0,1) == 1)):
                    relations += 1
                    trust.append([i,j])
                    if relations == max_relations:
                        abort = True
                        break
                if abort:
                    break
            if abort:
                break

        tests.append(n.__str__() + "\n" + trust.__str__().replace(' ', ''))

    return '''
'''.join(tests)
