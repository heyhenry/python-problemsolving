import random

"""
Simple rock, paper and scissors game with a definitive winner without retries but ensures the user plays a valid hand.
"""

options = ['rock', 'paper', 'scissors']
cpu_choice = random.choice(options)
choice = 0
ai_player = 'Ted'

print('Welcome to RPS!')
print('---------------')
print('You will be facing off against our champion ai player, Ted')
username = input('Please enter your username brave player: ')

while choice != 1 or choice != 2 or choice != 3:

    print('Make your choice between rock, paper and scissors by entering its associated number: ')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    choice = (int(input()))

    if choice == 1:
        choice = 'rock'
        break
    elif choice == 2:
        choice = 'paper'
        break
    elif choice == 3:
        choice = 'scissors'
        break
    else:
        print('You must choose a valid option.\n')

if choice == cpu_choice:
    print('Tie!')
elif choice == 'rock' and cpu_choice == 'scissors':
    print(username + ' has won RPS against Ted!')
elif choice == 'paper' and cpu_choice == 'rock':
    print(username + ' has won RPS against Ted!')
elif choice == 'scissors' and cpu_choice == 'paper':
    print(username + ' has won RPS against Ted!')
else:
    print('Ted has won the RPS match! He is still undefeated!')
    
print('Game Summary: ')
print(username + ' had played ' + choice)
print('Ted had played ' + cpu_choice)
print('--------------------------------')
