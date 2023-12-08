import random

print("[ Welcome to Rock, Paper and Scissors! ]")
username = input("Enter username: ")

ready_up = input("Are you ready to battle " + username + "? (y/n)")

if ready_up.lower() == 'yes' or ready_up.lower() == 'y':
    
    rps = ['paper', 'scissors', 'rock']
    ai = rps[random.randint(0,2)]
    game_start = True
    rounds = 1

    print("Game Start!")
    print(ai)
    while game_start:
    
        user_choice = input("Rock, Paper or Scissors? ")

        if user_choice.lower() == ai:
            print("Draw! Go again")
            rounds += 1
        elif user_choice.lower() == 'rock' and ai != 'paper':
            game_start = False
            print("You win!")
        elif user_choice.lower() == 'paper' and ai != 'scissors':
            game_start = False
            print("You win!")
        elif user_choice.lower() == 'scissors' and ai != 'rock':
            game_start = False
            print("You win!")
        else:
            print("The ai won!")
            game_start = False

else:
    print("Alrighty, ending the program for now.")


