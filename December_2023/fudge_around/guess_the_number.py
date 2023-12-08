import random

random_num = random.randint(0, 100)
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

print("\nSummary")
print("=======")    
print("Random Number: " + str(random_num))
print("Guess Attempts: " + str(attempts))

