import random

'''
1971 - Find if Path Exists in Graph
'''
def generate() -> str:
    tests = []
    max_num = 200
    min_num = 1
    edgecount_max = 200 # 2*10**5

    for n in [min_num, 2, 20, 45, 90, max_num]:
      graph = []
      edgecount = 0
      possible_edges = n*(n+1)
      allowed_edge_fraction = min(0.7,  edgecount_max / possible_edges) * 1000000
      for f in range(0, n):
        for t in range(f+1, n):
          if random.randint(1, 1000000) < allowed_edge_fraction:
             edge = [f,t]
             random.shuffle(edge)
             graph.append(edge)
      test = f"{n}\n{graph}\n0\n{n-1}".replace(' ', '')
      tests.append(test)
    
    graph = []
    for f in range(0, n-1):
        graph.append([f, f+1])
    test = f"{n}\n{graph}\n0\n{n-1}".replace(' ', '')
    tests.append(test)
    
    graph = []
    for f in range(0, n-10):
        graph.append([f, f+1])
    test = f"{n}\n{graph}\n{n-5}\n{n-5}".replace(' ', '')
    tests.append(test)
    
    return '''
'''.join(tests)
