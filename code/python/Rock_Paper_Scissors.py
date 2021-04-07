'''
My TODO LIST:
This sucks but hey I made it at least am pro coder 😎
when I was stuck I used this website: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
Rock Paper Scissors with bot
1. I need random with the bot with a choice or randint (randint is easier to use)
2. many functions for bot and gamer / player optinal/ a lot of if statements making a while loop
3. add user ability to play
'''

from random import randint

# welcome for gamers
def welcome():
    print("wassup gamers 🎮 are you able to beat the hard AI named Joe mama 👁️👄👁️   ? good luck gamers 🎮")
    print("also you have to put caps or your not a true gamer\n")

welcome()

# if they Typed these with caps it will play

bot = ["Rock", "Paper", "Scissors"]

# AI 
AI = bot[randint(0,2)]
# gamer why I named this why not yall gamers also this means player as well lol
gamer = False

# type(gamer)

# Debugging
# how the game will run
# the while loop

while gamer == False:
    # user interface
    gamer = input("Rock, Paper, Scissors: ")

    # if elif else statement
    if (AI == gamer):
        print("You tied with a bot! uhhhhhh")

    if (AI == "Rock")and(gamer == "Paper"):
        print("Pog you beat a bot!😲")

    elif (AI == "Paper")and(gamer == "Scissors"):
        print("Pog you beat a bot!😲")

    elif (AI == "Scissors")and(gamer == "Rock"):
        print("Pog you beat a bot!😲")

    elif (AI == "Paper")and(gamer == "Rock"):
        print("You really lost to a bot unpog 😢")

    elif (AI == "Scissors")and(gamer == "Paper"):
        print("You really lost to a bot unpog 😢")

    elif (AI == "Rock")and(gamer == "Scissors"):
        print("You really lost to a bot unpog 😢")
    
    else:
        print("bruh what did you put!")

    gamer = False
    AI = bot[randint(0,2)]
