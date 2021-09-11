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
      

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
