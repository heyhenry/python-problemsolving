import random

random_num = random.randint(0, 10)
not_num = True
attempts = 0
while not_num:
    user_input = int(input("Guess a number between 0 - 10: "))
    attempts += 1
    if user_input == random_num:
        print("You guessed the number!")
        not_num = False
    elif user_input < random_num:
        print("You guessed too low..")
    elif user_input > random_num:
        print("You guessed too high..")
    
print("The number was " + str(random_num))
print("It took you " + str(attempts) + " attempts to guess the correct number.")

