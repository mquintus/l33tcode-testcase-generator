'''
1361 - Validate Binary Tree Nodes
'''
def generate() -> str:
    tests = [
'''3
[2, 0, -1]
[-1, -1, -1]''',
'''4
[1,-1,3,-1]
[2,-1,-1,-1]''',
'''4
[1,-1,3,-1]
[2,3,-1,-1]''',
'''2
[1,0]
[-1,-1]''',
'''3
[2, 1, -1]
[-1, -1, -1]''',
'''3
[1,0,-1]
[-1,-1,-1]''',
'''4
[1, -1, -1, -1]
[2, -1, -1, -1]''',
'''4
[1, -1, 3, -1]
[-1, -1, -1, 2]''',
    ]
    
    return '''
'''.join(tests)
