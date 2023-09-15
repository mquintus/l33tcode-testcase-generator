import random

# 332 - Reconstruct Itinerary
#
# This is a graph problem.
# There are at max 300 edges given in random order.
# The first node is "JFK"
# There must be a path from "JFK" using all edges.

def generate() -> str:
    tests = []
    max_length = 300

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
    airport_codes = [
        'LAX', 'ORD', 'ATL', 'SFO', 'DFW', 'DEN', 'SEA', 'LAS', 'MCO', 'MIA', 'PHX', 'HAM',
        'IAH', 'EWR', 'DTW', 'MSP', 'BOS', 'CLT', 'PHL', 'LGA', 'FLL', 'BWI', 'SCL', 'IAD',
        'SAN', 'MDW', 'TPA', 'HNL', 'PDX', 'STL', 'OAK', 'MCI', 'SMF', 'CLE', 'MSY', 'RDU',
        'PIT', 'SJU', 'SNA', 'SAT', 'ANC', 'RSW', 'CVG', 'BUF', 'IND', 'AUS', 'CMH', 'PBI',
    ]
    while len(airport_codes) < 300:
        code = "".join([random.choice(letters), random.choice(letters), random.choice(letters)])
        if code not in airport_codes:
            airport_codes.append(code)
    airport_codes.sort()
    airport_codes.reverse()

    test = []
    route = []
    route.append("JFK")
    route.extend(airport_codes[0:100])
    route.append("JFK")
    route.extend(airport_codes[101:200])
    route.append("JFK")
    route.extend(airport_codes[201:300])
    for i in range(1, len(route)):
        test.append([route[i - 1], route[i]])
    tests.append(test.__str__().replace("'", '"').replace(" ", ''))

    test = []
    route = []
    l = 3
    for parts in range(l, 299 - (300 // l), l):
        route.append("JFK")
        route.extend(airport_codes[parts - l:parts])
    for i in range(1, len(route)):
        test.append([route[i - 1], route[i]])
    tests.append(test.__str__().replace("'", '"').replace(" ", ''))

    test = []
    route = []
    l = 149
    for parts in range(l, 299 - (300 // l), l):
        route.append("JFK")
        route.extend(airport_codes[parts - l:parts])
    for i in range(1, len(route)):
        test.append([route[i - 1], route[i]])
    tests.append(test.__str__().replace("'", '"').replace(" ", ''))

    # Random routes
    for _ in range(4):
        test = []
        route = []
        airport_codes.append("JFK")
        route.append("JFK")
        for i in range(299):
            route.append(random.choice(airport_codes))
        for i in range(1, len(route)):
            if route[i - 1] == route[i]:
                continue
            test.append([route[i - 1], route[i]])
        tests.append(test.__str__().replace("'", '"').replace(" ", ''))

    return "\n".join(tests)
