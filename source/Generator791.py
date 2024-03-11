import random

'''
791 - Custom Sort String
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = 200

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Edge case 1 - String length is minimal
    order = "a"
    string = "a"
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 2 - Short string needs to be reversed
    order = "ba"
    string = "ab"
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 3 - Order and String don't overlap
    order = "abcdefg"
    string = "hijklmnop" * 20
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 4 - Order and String do overlap, but nothing to do
    order = "abcdefg" + "qrstuv"
    string = "hijklmnop" * 20 + "qqqrrrssstttuuuvvv"
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 5 - Order and String do overlap, letters need reverse
    order = ("abcdefg" + "qrstuv")[::-1]
    string = "hijklmnop" * 20 + "qqqrrrssstttuuuvvv"
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 6 - Order and String do overlap, letters need reverse
    order = ("abcdefg" + "qrstuv")[::-1]
    string = "hijklmnop" * 10 + "qqqrrrssstttuuuvvv"*5
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 7 - String is totally shuffled
    order = ("abcdefg" + "qrstuv")[::-1]
    string = list("hijklmnop" * 10 + "qqqrrrssstttuuuvvv"*5)
    random.shuffle(string)
    string = "".join(string)
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)

    # Edge case 8 - String is totally shuffled
    order = ("abcdefgxyz" + "qrstuv")[::-1]
    string = list("hijklmnopxyz" * 8 + "qqqrrrssstttuuuvvv"*5)
    random.shuffle(string)
    string = "".join(string)
    test = '"{order}"\n"{string}"'.format(order=order, string=string)
    tests.append(test)


    return '''
'''.join(tests)
