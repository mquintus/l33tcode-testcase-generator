import random

'''
79 - Word Search
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 6
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += alphabet.lower()
    minval = 1
    maxval = 15

    # Testcase 1: Minimal board (success)
    board = ["A"]
    board = [list(row) for row in board]
    word = "A"
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 2: Minimal board (failure)
    board = ["i"]
    board = [list(row) for row in board]
    word = "I"
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 2: 2x6 Minimal board (failure)
    board = ["groarr","groarr"]
    board = [list(row) for row in board]
    word = "ooaarra"
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 3: 2x2 board (success)
    board = ["AB", "CD"]
    word = "ACDB"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 4: 2x2 board (failure)
    board = ["AB", "CD"]
    word = "ABDCA"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 5: 3x3 board (success)
    board = ["aaa","AAA","aaa"]
    word = "aAaaaAaaA"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 6: 3x3 board (success)
    board = ["abc","hid","gfe"]
    word = "abcdefghi"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 7: 4x4 board (success)
    board = ["zabc","yhid","xgfe","wvut"]
    word = "uvwxyzabcdefghi"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 7: 4x4 board (success)
    board = ["zibc","yhad","xgfe","wvut"]
    word = "uvwxyzibcdefgha"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 7: 4x4 board (success)
    board = ["aibc","yhzd","xgfe","wvut"]
    word = "uvwxyaibcdefghz"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 6: 4x4 board (failure)
    board = ["BDTA","ATCS","ADEE","ADEE"]
    word = "TDBATC"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 7: 6x6 board (success)
    board = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZabcd", "efghij"]
    word = "ABCDEFLKJIHGMNO"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 8: 6x6 board (failure)
    board = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZabcd", "efghij"]
    word = "efghijdXRLFEKQR"
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 9: 6x6 board (success)
    board = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZabcd", "efghij"]
    word = (board[-1] + board[-2][::-1] + board[-3])[:maxval]
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 10: 6x6 board (repetition)
    board = ["z"*6, "z"*6, "z"*6, "z"*6, "z"*4+"a"+"z", "z"*6]
    word = "z"*6 + "a" + "z"*5
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    # Testcase 11: 6x6 board (repetition)
    board = ["abzzzz", "b" + "z"*5, "z"*6, "z"*6, "z"*4+"a"+"b", "z"*5+"b"]
    word = "z"*6 + "bba" + "z"*5
    board = [list(row) for row in board]
    test = f'{board}\n"{word}"'
    tests.append(test.replace(' ', '').replace("'", '"'))

    return '''
'''.join(tests)
