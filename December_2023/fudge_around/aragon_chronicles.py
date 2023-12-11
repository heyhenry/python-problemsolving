"""
The first installment of a text based adventure game with choices for the Aragon Chronicles Series
"""
import time

# variables
username = ''
hearts = 5
mana = 1
inventory = ['guiding stick']

# the game 
username = input("Enter your adventurer's name: ")

loading = ["Loading... 0%", "Loading... 5%", "Loading... 10%", "Loading... 30%", "Loading... 50%", "Loading... 70%", "Loading... 100%", "Loaded!"]

for i in loading:
    print(i)
    time.sleep(0.8)

print("[ Welcome To Aragon Chronicles! ]")

