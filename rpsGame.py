import random
import sys
import os


def banner():
    print("""
	█▀█ █▀█ █▀▀ █▄▀
	█▀▄ █▄█ █▄▄ █░█

	█▀█ ▄▀█ █▀█ █▀█ █▀▀ █▀█
	█▀▀ █▀█ █▀▀ █▀▀ ██▄ █▀▄

	█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
	▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█""")


def clear_output():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def userInput(player_move=""):
    counter = 0
    while player_move != "r" and player_move != "p" and player_move != "s":
        if counter != 0:
            print("Type one of r, p, s or q")
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit", end=" -> ")
        player_move = input()
        if player_move == "q":
            sys.exit()
        counter += 1
    return player_move


if __name__ == "__main__":
    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0
    banner()
    while True:
        player_move = userInput()
        clear_output()
        banner()
        print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

        if player_move == "r":
            print("\tRock versus....")
        elif player_move == "p":
            print("\tPaper versus.....")
        elif player_move == "s":
            print("\tScissors versus....")

        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computer_move = "r"
            print("\tRock")
        elif randomNumber == 2:
            computer_move = "p"
            print("\tPaper")
        elif randomNumber == 3:
            computer_move = "s"
            print("\tScissors")
        if player_move == computer_move:
            print("\tIt's a tie")
            ties = ties+1
        elif player_move == "s" and computer_move == "p":
            print('\tYou win!!!')
            wins = wins+1
        elif player_move == "p" and computer_move == "r":
            print("\tYou win!!!")
            wins = wins+1
        elif player_move == "r" and computer_move == "s":
            print("\tYou win!!!")
            wins = wins+1
        elif player_move == "s" and computer_move == "r":
            print("\tYou losse!!!")
            losses = losses+1
        elif player_move == "r" and computer_move == "p":
            print("\tYou losse!!!")
            losses = losses+1
        elif player_move == "p" and computer_move == "s":
            print("\tYou losse!!!")
            losses = losses+1
