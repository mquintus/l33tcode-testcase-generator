import random

'''
2092 - Find All People With Secret
'''
def generate() -> str:
    tests = []
    min_num = 2
    max_num = 200
    curr_time = 1
    max_meetings = 200
    for n in [min_num, min_num + 11, max_num - 1, max_num]:
        firstPerson = random.randint(1, n-1)
        possible_meetings = []
        knowing = [firstPerson, 0]
        for i in range(max_meetings // 2):
            if random.randint(0, 1) == 1:
                curr_time += 1
            for d in range(2):
                next_person = random.randint(1, n-1)
                prev_person = random.choice(knowing)
                if next_person == prev_person:
                    continue
                knowing.append(next_person)
                if d == 1:
                    next_person, prev_person = prev_person, next_person
                possible_meetings.append([next_person,prev_person,curr_time])
        random.shuffle(possible_meetings)
        meetings = []
        for i in range(min(len(possible_meetings), max_num)):
            meetings.append(possible_meetings[i])
        tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', '') + "\n" + firstPerson.__str__())

        firstPerson = 1
        possible_meetings = []
        curr_time = 1000
        for i in range(n):
            for j in range(0, i):
                if i!=j and (len(possible_meetings) == 0 or random.randint(0, 1) == 1):
                    possible_meetings.append([i,j,curr_time])
                    curr_time -= 1
        random.shuffle(possible_meetings)
        possible_meetings = possible_meetings[:max_meetings]
        possible_meetings.sort(key=lambda x: x[2])
        curr_time = 100 * random.randint(3,8)
        for p in possible_meetings:
            p[2] = curr_time
            curr_time += 9
        meetings = []
        for i in range(min(len(possible_meetings), max_num)):
            meetings.append(possible_meetings[i])
        tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', '') + "\n" + firstPerson.__str__())

    return '''
'''.join(tests)
