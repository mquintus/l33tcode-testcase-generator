import random

'''
13 - Roman to Integer
'''

_ROMAN_TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90,  "XC"), (50,  "L"), (40,  "XL"),
    (10,  "X"),  (9,   "IX"), (5,   "V"), (4,   "IV"),
    (1,   "I"),
]

def int_to_roman(n: int) -> str:
    res = []
    for val, sym in _ROMAN_TABLE:
        while n >= val:
            res.append(sym)
            n -= val
    return "".join(res)

def generate() -> str:
    min_val = 1
    max_val =3999
    return f'"{int_to_roman(random.randint(min_val, max_val))}"'
