import random
import time

# List for guestion word
weather = ["climate", "isobar", "visibility",
           "showery", "unsettled", "reinbow"]
irish_names = ["caoimhe", "saoirse", "clodagh",
               "roisin", "eireann", "padraig"]
counties_of_ireland = ["limerick", "tipperary", "wexford",
                       "donegal", "longford", "galway"]   

category = [weather, irish_names, counties_of_ireland]    


def display_greeting():
    """
    Prompt user to input name and greetings
    """
    print("WELCOME TO")
    # Title ASCII ART 
    print(" ▄  █ ██      ▄     ▄▀  █▀▄▀█ ██      ▄")       
    print("█   █ █ █      █  ▄▀    █ █ █ █ █      █")      
    print("██▀▀█ █▄▄█ ██   █ █ ▀▄  █ ▄ █ █▄▄█ ██   █")     
    print("█   █ █  █ █ █  █ █   █ █   █ █  █ █ █  █")    
    print("   █     █ █  █ █  ███     █     █ █  █ █")     
    print("  ▀     █  █   ██         ▀     █  █   ██")    
    print("       ▀                       ▀")

    name = input("Enter your name:")
    print("Hello" + name + "Best of luck!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")


def display_instructions():
    """
    Ask user if instruction is need and displays instruction as requested
    """
    print("Do you need instructions before starting a game?")
    instruction_on = input("Press y if yes, any other key to play game : \n")
    if instruction_on.lower() == "y":
         instructions_txt()
         print("Are you ready to play?")
         game_start = input("Press Any key to start a game >> \n")
    else:
        pass


def instructions_txt():
    """
    Display instructions
    """
    print("Here is instruction on how to play \n"
          "1. Choose a category\n"
          "2. The same number of Underscores '_' will be displayed \n"
          "   as letters in the word.\n"
          "3. Guess the word\n"
          "   Only one alphabet key should be entered at each time.\n"
          "   Space between the words is considered incorrect.\n"
          "4. If your answer is correct, the letter will be displayed\n"
          "   instead of the underscore'_'.\n"
          "5. If you guess all the letters and complete the word,\n"
          "   you win the game\n"
          "6. If the incorrect answer is entered,"
          " the hangman image will progress.\n"
          "7. If the number of incorrect attempts reaches the limit\n"
          "   and hangman image completes, game over!")
    
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
