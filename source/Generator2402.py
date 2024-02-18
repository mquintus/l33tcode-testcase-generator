import random

'''
2402 - Meeting Rooms III
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 100000
    minval = 1
    maxval = 100000
    
    # Testcase 1 
    # A few overlapping meetings all of the same duration
    n = 100
    meetings = [
        [i, i + 5] for i in range(random.randint(20,30))
    ]
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))

    # Testcase 2
    # The minimal testcase
    n = 1
    start = random.randint(minval, maxval - 1)
    end = random.randint(start, maxval)
    meetings = [[start, end]]
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))

    # Testcase 3 
    # 100 rooms and all are full the whole time,
    # only room 99 has short meetings
    n = 100
    meetings = [[i, random.randint(200, 999)] for i in range(1, 100)]
    meetings.append([100, 101])
    meetings.append([101, 102])
    meetings.append([102, 105])
    meetings.append([103, 104])
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))
   
    # Testcase 4
    # Only two rooms but many meetings
    n = 2
    meetings = [[i, i + random.randint(20, 999)] for i in range(1, 100)]
    random.shuffle(meetings)
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))

    # Testcase 5
    # Many rooms, many meetings
    n = 50
    meetings = [[i*100, i*100 + random.randint(200, 999)] for i in range(1, 150)]
    random.shuffle(meetings)
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))

    # Testcase 6
    # All rooms are full all the time
    n = 100
    meetings = [[i, 100000] for i in range(1, 125)]
    random.shuffle(meetings)
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))

    # Testcase 6
    # All rooms are full all the time
    n = 100
    meetings = [[i*10, i*10 + random.randint(1,4567)] for i in range(1, 1000)]
    random.shuffle(meetings)
    tests.append(n.__str__() + "\n" + meetings.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
