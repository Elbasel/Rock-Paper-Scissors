import random

ratings = dict()
with open('ratings.txt', 'a+') as ratings_file:
    ratings_file.seek(0)
    for line in ratings_file:
        name, rating = line.split()
        ratings[name] = rating

player_name = input('Enter your name: ')
player_rating = ratings.get(player_name, 0)

print(f'Hello, {player_name}')

rules = input('Enter Game Rules: ')

if rules:
    rules = rules.split(',')

    # key(a rule): value(a list of rules that can win over the key rule)
    winning_conditions = {}

    split_index = (len(rules) - 1) // 2

    # Extracting the rules that will be stronger than the loop variable's rule.
    for rule_index, rule in enumerate(rules):

        rule_list = rules[rule_index + 1:] + rules[:rule_index]  # Elems after rule + elems before rule

        stronger_rules = rule_list[:split_index]  # All the rules that will win over the loop variable's rule

        winning_conditions[rule] = stronger_rules

else:
    # Set everything to default values.
    rules = ['rock', 'paper', 'scissors']
    winning_conditions = {'rock': ['paper'], 'paper': ['scissors'], 'scissors': ['rock']}

print("Okay, let's start")


while True:

    hand = input('>')

    if hand == '!exit':
        break
    elif hand == '!rating':
        print(f'Your rating: {player_rating}')
        continue
    elif hand not in rules:
        print('Invalid input')
        continue

    computer = random.choice(rules)

    if hand == computer:
        player_rating += 50
        print(f'There is a draw ({computer})')
    elif hand in winning_conditions[computer]:
        player_rating += 100
        print(f'Well done. Computer chose {computer} and failed')
    else:
        print(f'Sorry, but computer chose {computer}')

ratings[player_name] = player_rating
with open('ratings.txt', 'w') as ratings_file:
    for name, rating in ratings.items():
        ratings_file.write(name + ' ' + str(rating) + '\n')
