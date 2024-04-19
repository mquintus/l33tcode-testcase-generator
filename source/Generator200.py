import random

'''
200 - Number of Islands
'''
def generate() -> str:
    tests = []

    max_width = 300
    max_height = 300

    for width, height in [
(1, 1),
(1,20),
(23,1),
(max_width,2),
(27,13),
(max_width,max_height),
    ]:
      grid = [[random.choice(["0","1"]) for _ in range(width)] for _ in range(height)]
      tests.append(grid.__str__().replace(' ', '').replace("'", '"'))

    grid = []
    curr_start = "1"
    for _ in range(height):
      row = []
      curr = curr_start
      if curr_start == "1":
        curr_start = "0"
      else:
        curr_start = "1"
      for _ in range(width):
        row.append(curr)
        if curr == "1":
          curr = "0"
        else:
          curr = "1"
      grid.append(row)  
    tests.append(grid.__str__().replace(' ', '').replace("'", '"'))

#    width = 20
#    height = 13      
    grid = [["1"] * width for _ in range(height)]
    px,py = 0,0
    while px < width-1 or py < height-1:
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
        grid[py][px] = "0"
    tests.append(grid.__str__().replace(' ', '').replace("'", '"'))
    
    return '''
'''.join(tests)
