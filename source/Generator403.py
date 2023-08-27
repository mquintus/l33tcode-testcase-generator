import random

'''
Frog Jump
'''
def generate() -> str:
    tests = []
    max_stones = 2_000
    max_distance = 2**32



    tests.append([0,2147483647].__str__())

    stones = [0,1,2,4,7,11,15,20,25,30,35,41,45,50]
    for distance in range(380_000, 381_900):
        stones.append(distance)
    tests.append(stones.__str__())

    # max distance
    speed = 0
    distance = 0
    stones = []
    for jump in range(2000):
        stones.append(distance)
        speed += 1
        distance += speed
    tests.append(stones.__str__())


    # two path solution
    stones = [0,1,2,4,7,11]
    distance = 15
    for speed in range(4, 2000 // 2 - 5):
        stones.append(distance - 3)
        stones.append(distance)
        distance += speed
    stones.append(distance - 4)
    distance += speed
    stones.append(distance - 4)
    distance += speed
    stones.append(distance - 4)
    distance += speed
    stones.append(distance - 4)
    distance += speed
    tests.append(stones.__str__())

    # three connected paths solution
    stones = [0,1,2,4,7,11]
    distance = 15
    for speed in range(4, 2000 // 3):
        stones.append(distance - 1)
        stones.append(distance)
        stones.append(distance + 1)
        distance += speed
    tests.append(stones.__str__())

    # random speed change (tweeked towards speed up)
    for _ in range(0, 3):
        stones = []
        new_stones = [[0, 0]]
        stone_count = 0
        k = 1
        while stone_count < max_stones:
            stone, speed = new_stones.pop()
            if stone not in stones:
                stones.append(stone)
                stone_count += 1

            if speed < 1:
                speed = 1
                new_stones.append((stone + speed, speed,))
            elif speed == 1:
                for w in [speed + 1]:
                    new_stones.append((stone + w, w,))
            else:
                w = min(speed + 1, random.randint(speed - 1, speed + 5))
                new_stones.append((w + stone, w,))
        tests.append(stones.__str__())


    return "\n".join(tests)
