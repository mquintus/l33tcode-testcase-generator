import random

# 1376. Time Needed to Inform All Employees
def generate() -> str:
    tests = []
    max_length = 100_000
    max_num = 1_000
    min_num = 0

    for case in range(2):
        n = max_length
        headID = random.randint(0,max_length-1)
        print("headID", headID)
        prev_layer = [headID]
        number_layers = int(max_length / (case + 5.5))
        print("number_layers", number_layers)
        remaining_persons = [i for i in range(n)]
        #random.shuffle(remaining_persons)
        remaining_persons.remove(headID)
        manager = [headID] * n
        manager[headID] = -1
        informTime = [0] * n

        personsPerLayer = max_length // number_layers
        for l in range(number_layers):
            #print("Layer", l, "with", personsPerLayer, "persons...")
            for person in remaining_persons[:personsPerLayer]:
                m = prev_layer[person % len(prev_layer)]
                informTime[m] = random.randint(min_num,max_num)
                manager[person] = m
            prev_layer = remaining_persons[:personsPerLayer]
            remaining_persons = remaining_persons[personsPerLayer:]
            #print("remaining_persons:", len(remaining_persons))
        print("Layer", l, "with", personsPerLayer, "persons...")
        print("remaining_persons:", len(remaining_persons))

        test = f"{n}\n{headID}\n{manager}\n{informTime}".replace(" ", "")
        tests.append(test)

    return "\n".join(tests)
