import random

'''
2353 - Design a Food Rating System
'''
def generate() -> str:
    tests = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    food_min = 1
    food_max = 2 * 10**4

    rating_min = 1
    rating_max = 100000

    actions_max = 2 * 10**4

    food_options = list(set([
        ' '.join([random.choice(alphabet) for _ in range(random.randint(1, 10))]) for _ in range(food_max + 1)
    ]))
    while len(food_options) < food_max:
        food_options.append(' '.join([random.choice(alphabet) for _ in range(random.randint(1, 10))]))
        food_options = list(set(food_options))
    cuisine_options = list(set([
        ' '.join([random.choice(alphabet) for _ in range(random.randint(1, 10))]) for _ in range(food_max + 1)
    ]))
    action_options = ['changeRating', 'highestRated']

    for n in [10, 100, food_max - 2]:
        cuisine_options_local = cuisine_options[:n//4 + 1]
        for action_count in [n//2, n + 1]:
            test = []

            # initial action
            test_actions = ["FoodRatings"]
            test_params = []
            ratings = []
            foods = []
            cuisines = []
            for _ in range(n):
                ratings.append(random.randint(rating_min, rating_max))
                cuisines.append(f'{random.choice(cuisine_options_local)}')
            foods.extend(random.sample(food_options, n))
            test_params.append([foods, cuisines, ratings])

            # more actions
            for _ in range(action_count):
                action = random.choice(action_options)
                test_actions.append(action)
                if action == 'changeRating':
                    test_params.append([f'{random.choice(foods)}', random.randint(rating_min, rating_max)])
                elif action == 'highestRated':
                    test_params.append([f'{random.choice(cuisines)}'])

            test.append(test_actions.__str__().replace(' ', '').replace('\'', '"'))
            test.append(test_params.__str__().replace(' ', '').replace('\'', '"'))
            tests.append("\n".join(test))

    n = food_max
    cuisine_options_local = cuisine_options[:2]
    action_count = n
    test = []

    # initial action
    test_actions = ["FoodRatings"]
    test_params = []
    ratings = []
    foods = []
    cuisines = []
    for _ in range(n):
        ratings.append(random.randint(rating_min, rating_max))
        cuisines.append(f'{random.choice(cuisine_options_local)}')
    foods.extend(random.sample(food_options, n))
    test_params.append([foods, cuisines, ratings])

    # more actions
    newRating = 1
    for _ in range(action_count):
        newRating += 1
        action = random.choice(action_options)
        test_actions.append(action)
        if action == 'changeRating':
            test_params.append([f'{random.choice(foods[:2])}', newRating])
        elif action == 'highestRated':
            test_params.append([f'{random.choice(cuisines)}'])

    test.append(test_actions.__str__().replace(' ', '').replace('\'', '"'))
    test.append(test_params.__str__().replace(' ', '').replace('\'', '"'))
    tests.append("\n".join(test))


    return '''
'''.join(tests)
