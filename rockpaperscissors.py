import random
values = [1,2,3]
def show():
    print('1: Rock')
    print('2: Paper')
    print('3: Scissors')

show()

choice_player = int(input('What do you wanna choose: '))
choice_compuer = random.choice(values)

print('')
if(choice_compuer==1):
    choice = 'Rock'
if(choice_compuer==2):
    choice = 'Paper'
if(choice_compuer==3):
    choice = 'Scissors'

if(choice_player==1):
    choice1 = 'Rock'
if(choice_player==2):
    choice1 = 'Paper'
if(choice_player==3):
    choice1 = 'Scissors'
print('You chose ' + choice1 + '.')
print('Computer chose ' + choice + '.\n')

if(choice_player == choice_compuer):
    print('Its a tie!')


if(choice_player == 1 and choice_compuer == 2):
    print('You Lose')
if(choice_player == 1 and choice_compuer == 3):
    print('You Win')


if(choice_player == 2 and choice_compuer == 1):
    print('You Win')
if(choice_player == 2 and choice_compuer == 3):
    print('You Lose')


if(choice_player == 3 and choice_compuer == 1):
    print('You Lose')
if(choice_player == 3 and choice_compuer == 2):
    print('You Win')