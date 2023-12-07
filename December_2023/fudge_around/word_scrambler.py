import random

user_input = input("Enter words to be scrambled into a single 'word': ")

not_satisfied = True
user_choice = 0
counter = 0

while not_satisfied:
    
    counter += 1
    temp_words = [w for w in user_input if w != ' ']
    random.shuffle(temp_words)
    word = ''
    for w in temp_words:
        word += w

    print("\nNew generated word: " + word)
    print("====")
    print("1. Generate a new one")
    print("2. I like the word")
    user_choice = int(input("Are you satisfied with the generated word? "))

    if user_choice != 1 and user_choice != 2:
        print("Incorrect choice. We will proceed to generate a new word for you.")
    elif user_choice == 2:
        print("Thank you for using our service.")
        not_satisfied = False
    else: 
        continue

print("Summary Details: ")
print("-------")
print("Generated word chosen: " + word) 
print("Generated a total of " + str(counter) + " times.")
    

# things i can implement 
# 1. store list of all generated names and make it a selectable option to review list
# 2. automatically run through generated names and only stop when a key is pressed
# 3. option to select how many generated names you want generated in one go (i.e. 10 generated names at a time)