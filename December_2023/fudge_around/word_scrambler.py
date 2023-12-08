import random

user_input = input("Enter words to be scrambled into a single 'word': ")

not_satisfied = True
user_choice = 0
generations = 0
selected_word = ''
while not_satisfied:

    print("\nMenu")
    print("----")
    print("1. Generate 1 new word")
    print("2. Generate 5 new words")
    print("3. Exit")
    user_choice = input("Select an option between 1-3: ")
    generated_list = []
    if user_choice.isdigit():
        if int(user_choice) == 1:
            generations += 1
            temp_words = [w for w in user_input if w != ' ']
            random.shuffle(temp_words)
            word = ''
            for w in temp_words:
                word += w
            print("1 | " + word)
            print("\n1. Select generated word")
            print("2. Try again")
            user_list_choice = input("Do you wish to select this word: ")

            if user_list_choice == '1':
                selected_word = word
                not_satisfied = False
            elif user_list_choice == '2':
                print("Going back to main menu...")
            else:
                print("Invalid user input. Going back to the main menu..")
                 
        elif int(user_choice) == 2:
            generations += 5
            i = 0
            while i < 5:
                i += 1
                temp_words = [w for w in user_input if w != ' ']
                random.shuffle(temp_words)
                word = ''
                for w in temp_words:
                    word += w
                generated_list.append(word)
            for word in range(len(generated_list)):
                print(str(word + 1) + "|" + generated_list[word])
            print('6 | Return to Menu')
            user_list_choice = int(input("Selected desired generated word via their number: "))
            if user_list_choice > 0 and user_list_choice < 11:
                selected_word = generated_list[user_list_choice - 1]
                not_satisfied = False
    else:
        print("Invalid user input. Returning to menu..")    


    # if user_choice != 1 and user_choice != 2:
    #     print("Incorrect choice. We will proceed to generate a new word for you.")
    # elif user_choice == 2:
    #     print("Thank you for using our service.")
    #     not_satisfied = False
    # else: 
    #     continue

print("\nSummary Details: ")
print("-------")
print("Generated word chosen: " + selected_word) 
print("Generated a total of " + str(generations) + " times.")
    

# things i can implement 
# 1. store list of all generated names and make it a selectable option to review list
# 2. automatically run through generated names and only stop when a key is pressed
# 3. option to select how many generated names you want generated in one go (i.e. 10 generated names at a time)