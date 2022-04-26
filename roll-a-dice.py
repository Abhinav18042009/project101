import random

ch = "y"

while ch == 'y':
    y = random.randint(1,6)
    if y == 1:
        print('o')
    if y == 2:
        print('o')
        print(' o')
    if y == 3:
        print('o')
        print(' o')
        print('  o')
    if y == 4:
        print('o')
        print(' o')
        print('  o')
        print('   o')
    if y == 5:
        print('o')
        print(' o')
        print('  o')
        print('   o')
        print('    o')
    if y == 6:
        print('o')
        print(' o')
        print('  o')
        print('   o')
        print('    o')
        print('     o')
    ch = str(input('Do you want to roll a dice?:'))