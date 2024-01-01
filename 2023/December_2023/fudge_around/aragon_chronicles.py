"""
The first installment of a text based adventure game with choices for the Aragon Chronicles Series
"""
import time

# helper functions

# provide result from 2 given choices, else continue to repeat question
def make_choice(choice_one : str, choice_two: str) -> int:

    valid_choice = True
    choice = ''
    while valid_choice:

        print('[1]:' + choice_one)
        print('[2]:' + choice_two)
        choice = input("Select a Choice: ")

        if choice == '1' or choice == '2':
            valid_choice = False
        else:
            print("\nInvalid choice. Please enter number 1 or 2.")

    return choice

def main():

    # variables
    username = ''
    hearts = 5
    mana = 1
    inventory = ['guiding stick']

    # the game 

    # loading = ["Loading... 0%", "Loading... 5%", "Loading... 10%", "Loading... 30%", "Loading... 50%", "Loading... 70%", "Loading... 100%", "Loaded!"]

    # for i in loading:
    #     print(i)
    #     time.sleep(0.8)

    print("[ Welcome To Aragon Chronicles! ]")
    username = input("Enter your adventurer's name: ")
    
    print("You wake up in an unfamiliar surrounding. \nThe environment is cold and covered with an unknown purple mist.")
    print("There is something glowing next to you, but you are unable to see it clearly.")
    
    choice = make_choice("You decide to investigate what the glowing thing is.", "You decide to ignore it and begin wandering around.")
    if choice == '1':
        print("One Here")
    elif choice == '2':
        print("Two Here")

    print("End of cycle")

if __name__ == "__main__":
    main()


# look into the make_choice function and its counter part call in the main function. There is potentially some redudancy that can be reduced.