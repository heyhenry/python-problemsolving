import random


dice = random.randint(1, 6)

player_username = input("Please enter player username: ")
ai_username = 'Mr. Robot'

player_score = 0
ai_score = 0

winner = ''

running = True

while running:

    print("###############")
    input("Press 'Enter' to roll the die " + player_username + '!\n')
    
    dice = random.randint(1, 6)
    if dice == 1:
        player_score = 0
    print(player_username + " rolls a " + str(dice))
    player_score += dice
    
    dice = random.randint(1, 6)
    if dice == 1:
        ai_score = 0
    print(ai_username + " rolls a " + str(dice) + '\n')
    ai_score += dice

    print("###############")
    print("Player Score: " + str(player_score))
    print("AI Score: " + str(ai_score))

    if player_score >= 30:
        winner = player_username
        running = False
    elif ai_score >= 30:
        winner = ai_username
        running = False

print(winner + " wins!")


