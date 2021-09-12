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

# stages for wrong answer  https://enhancer298.net/2020/07/10/hangman1
stages = ['___________________',
          '|         |        ',
          '|         |        ',
          '|         |        ',
          '|         0        ',
          '|        /|＼      ',
          '|        / ＼      ',
          '| GAME        OVER!']

# Setting the stage number to be used as limit for incorrect attempts
stage_num = len(stages)


def display_greeting():
    """
    Prompt user to input name and greetings
    """
    print("WELCOME TO")
    # Title ASCII ART https://patorjk.com/software/taag
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


def category_select():
    """
    Prompt user to select a category for the game and validate the input
    """
    print("PLEASE CHOOSE ONE OF THE CATEGORY:\n")  
    print("1. Weather, 2. Irish names, 3. Counties of Ireland"
          "4. All the category mixed\n")
    category_num = 0
    while not 1 <= category_num <= 4:
        try:
            category_num = int(input("PLEASE ENTER 1, 2, 3 or 4  >>>  \n"))
            if 1 <= category_num <= 4:
                return category_num
            else:
                pass
         except ValueError as e:
            print("Only number 1, 2, 3 or 4 accepted")        


# Write your code to expect a terminal of 80 characters wide and 24 rows high
