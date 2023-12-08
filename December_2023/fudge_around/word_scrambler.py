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
    print("3. Exit\n")
    user_choice = input("Select an option between 1-3: ")
    
    generated_list = []
    
    # checks to see if the provided user input is a number, if so proceed validating the number
    if user_choice.isdigit():
        
        # first menu option
        if int(user_choice) == 1:
            is_single_generation = True
            # continuous loop through the single word generation option until condition a provided condition is met
            while is_single_generation:

                # records word generations
                generations += 1
                
                # list comprehension used to combine all provided words
                temp_words = [w for w in user_input if w != ' ']
                # rearrange the characters for the combined word in a random order
                random.shuffle(temp_words)
                word = ''
                # store the new word in a dedicated string variable in lieu of list
                for w in temp_words:
                    word += w
                
                # options to generate new words or proceed to finalise selected word
                print("1 | " + word)
                print("\n1. Select generated word")
                print("2. Try again")
                print("3. Go to menu")
                user_list_choice = input("\nDo you wish to select this word: ")

                if user_list_choice.isdigit():
                    if int(user_list_choice) == 1:
                        selected_word = word
                        not_satisfied = False
                        is_single_generation = False
                    elif int(user_list_choice) == 2:
                        print("\nRunning it back..")
                    elif int(user_list_choice) == 3:
                        print("\nReturning to menu..")
                        is_single_generation = False
                    else:
                        print("\nInvalid user input. Going back to the main menu..")
                        is_single_generation = False

        # second menu option    
        elif int(user_choice) == 2:
            
            # records word generations
            generations += 5
            i = 0

            # loops through to create 5 newly generated words to be placed in a list for review
            while i < 5:
                i += 1
                temp_words = [w for w in user_input if w != ' ']
                random.shuffle(temp_words)
                word = ''
                for w in temp_words:
                    word += w
                generated_list.append(word)
            
            # for loop integrated menu design for a dynamic flow of newly generated word display
            for word in range(len(generated_list)):
                print(str(word + 1) + "| " + generated_list[word])
            print('6| Return to Menu')
            
            user_list_choice = input("\nSelected desired generated word via their number: ")
            
            if user_list_choice.isdigit():
                if int(user_list_choice) > 0 and int(user_list_choice) < 6:
                    selected_word = generated_list[int(user_list_choice) - 1]
                    not_satisfied = False
                elif int(user_list_choice) == 6:
                    continue
    else:
        print("Invalid user input. Returning to menu..")    

# summary display of user usage
print("\nSummary Details: ")
print("-------")
print("Generated word chosen: " + selected_word) 
print("Generated a total of " + str(generations) + " times.\n")