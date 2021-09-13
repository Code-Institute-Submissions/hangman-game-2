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
    print("The game is about to start!\nLet's play Hangman!")


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
          " 4. All the category mixed\n")
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


def select_question():
    """
    Random word selection from the list and display _ for each letter
    """
    time.sleep(2)
    category_chosen = category_select()
    list_num = category_chosen - 1
    print(f"Category {category_chosen}  was chosen")
    if category_chosen == 4:
        category_item = random.choice(category)
        word = random.choice(category_item)
        return(word)
    else:
        category_item = category[list_num]
        word = random.choice(category_item)
        return(word)


def start_game():
    """
    Main game function to display questions, check the answer
    and count attempts.
    Repeats process if game completion condition is not met.
    Either word completion or reaching full stages will end the game.
    """
    incorrect = 0
    correct_guess = set([])
    word = select_question()
    check_answer = word.replace(" ", "")
    answers = [i for i in check_answer]
    wrong_guess = []
    while incorrect < stage_num:
        display_guess_message()
        """
        Print out _ for the remaining letters to guess
        """
        for i in word:
            if i == " ":
                print(i, end="  ")
            elif i in correct_guess:
                print(i.upper(), end=" ")
            else:
                print("_ ", end=" ")
        print('\n')
        guessed = input("Enter one letter! \n").lower()   
        if guessed in answers:
            if guessed in correct_guess:
                display_alredy_used()
                time.sleep(2)
            else:
                print(f"{guessed.upper()} is the right letter!")
                correct_guess.add(guessed)
                word_letters = word.replace(" ", "")
                if correct_guess == set(word_letters):
                    print(word.upper())
                    print(f"CONGRATULATIONS! "
                          f"You have guessed the word {word.upper()}. YOU WIN!")
                    break
                time.sleep(2)          
        else:
            if len(guessed) > 1:
                print("Enter only one letter at a time")
            else:
                print(f"' {guessed.upper()}' is not in correct answer!")

            incorrect += 1
            print("\n".join(stages[:incorrect]))
            print("\n")
            wrong_guess.append(guessed.upper())
            print(f"Your incorrect guesses: {wrong_guess} ")
            time.sleep(2)
    if incorrect == stage_num:
        print(f"Answer is {word.upper()}")
        game_over()

    time.sleep(3)
    replay()


def display_guess_message():
    print("\n")
    print("Can you guess the word?")
    print("Enter one letter to see are you right?")


def display_alredy_used():
    print("You have already used this letter before,"
          " it's already displayed!")


def game_over():
    """
    GAME OVER ascii art
    """
    print(" _____ ____  _      _____   ____  _     _____ ____")
    print("/  __//  _ \/ \__/|/  __/  /  _ \/ \ |\/  __//  __\ ")
    print("| |  _| / \|| |\/|||  \    | / \|| | //|  \  |  \/|")
    print("| |_//| |-||| |  |||  /_   | \_/|| \// |  /_ |    /")
    print("\____\\_/ \|\_/  \|\____\  \____/\__/  \____\\_/\_\\n")


def replay():
    print("Would you like to play again?")
    print("Enter y or press RUN PROGRAM button above to play again."
          "or press any other key to exit the game.")
    play_again = input(
        "Please press y to play, any other key to exit the game \n")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Hope you enjoyed the game!")


def main():
    display_greeting()  # greeting function
    display_instructions()  # display instruction if user chooses
    start_game()


main()    

# Write your code to expect a terminal of 80 characters wide and 24 rows high
