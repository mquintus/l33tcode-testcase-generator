import random

'''
463 - Island Perimeter
'''
def generate() -> str:
    tests = []

    max_width = 100
    max_height = 100

    for width, height in [
(1, 1),
(1,20),
(23,1),
(2,50),
(max_width,2),
(27,13),
(max_width,max_height),
    ]:
      grid = [[0] * width for _ in range(height)]
      px,py = 0,0
      grid[py][px] = 1
      while px < width-1 or py < height-1:
#       print(px, py)
        step = random.choice([-1,1,1,1])
        axis = random.randint(0,1)
        if axis == 0:
          px += step
          px = max(0, px)
          px = min(width-1, px)
        else:
          py += step
          py = max(0, py)
          py = min(height-1, py)
        grid[py][px] = 1
      tests.append(grid.__str__().replace(' ', ''))

    width = 20
    height = 13      
    grid = [[1] * width for _ in range(height)]
    px,py = 0,0
    while px < width//2 and py < height//2:
#       print(px, py)
        step = 1
        axis = random.randint(0,1)
        if axis == 0:
          px += step
          px = max(0, px)
          px = min(width-1, px)
        else:
          py += step
          py = max(0, py)
          py = min(height-1, py)
        grid[py][px] = 0
    tests.append(grid.__str__().replace(' ', ''))
    
    return '''
'''.join(tests)
