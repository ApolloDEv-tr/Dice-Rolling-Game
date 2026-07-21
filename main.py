import random

while True:
    roll = input('Roll? y/n ')
    if roll.lower() == 'y': 
        rolls = random.randint(1, 6), random.randint(1, 6)
        print('You rolled', rolls)
    else:
        break
