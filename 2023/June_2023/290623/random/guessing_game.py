import random 

def main():

    random_num = random.randint(1, 1000)

    counter = 0
    outcome = ''

    print('You have 5 chances to guess the correct number and win a prize!')
    print(random_num)
    
    while counter != 5:
        counter += 1

        choice = int(input("Choose a number between 1 - 1000 "))

        if choice == random_num:
            print('Congratulations you guessed correctly and have won a prize!')
            break
        else:
            print("Aw that's not the correct number!")
        
    if counter < 6 and choice == random_num:
        outcome = 'Winner'
    else:
        outcome = 'Loser'

    print('Results Summary: ')
    print('================')
    print('Attempts used: ' + str(counter))
    print('Random number: ' + str(random_num))
    print('Outcome: ' + outcome)    

if __name__ == "__main__":
    main()