import random
import time

# List for guestion word
weather = ["climate", "isobar", "visibility",
           "showery", "unsettled", "rainbow"]
irish_names = ["caoimhe", "saoirse", "clodagh",
               "roisin", "eireann", "padraig"]
counties_of_ireland = ["limerick", "tipperary", "wexford",
                       "donegal", "longford", "galway"]
drinks = ["tequila", "vermouth", "cognac",
          "whiskey", "water", "baileys"]

category = [weather, irish_names, counties_of_ireland, drinks]

# stages for wrong answer  https://enhancer298.net/2020/07/10/hangman1
stages = ['___________________',
          '|         |        ',
          '|         |        ',
          '|         |        ',
          '|         0        ',
          '|        /|＼      ',
          '|        / ＼      ',
          '|      THE END     ']

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

    name = input("Enter your name:")
    print(f"Hello {name.upper()}, Best of luck!")
    time.sleep(2)
    print("GET EXCITED!\nLet's play Hangman!")


def display_rules():
    """
    Ask user if game rules is need and displays game rules as requested
    """
    print("Do you want to know the game's rules?")
    rules_on = input("Press y if yes,"
                     "or any other key to play the game:\n")
    if rules_on.lower() == "y":
        rules_txt()
        print("Are you ready to play?")
        input("Press any key to start the game >> \n")
    else:
        pass


def rules_txt():
    """
    Display game rules
    """
    print("Here are rules on how to play \n"
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
          "   the hangman image will progress.\n"
          "7. If the number of incorrect attempts reaches the limit\n"
          "   and hangman image completes, game over!")


def category_select():
    """
    Prompt user to select a category for the game and validate the input
    """
    print("PLEASE CHOOSE ONE OF THE CATEGORY:\n")
    print("1. Weather, 2. Irish names, 3. Counties of Ireland", "4. Drinks\n",
          "5. All the category mixed\n")
    category_num = 0
    while not 1 <= category_num <= 5:
        try:
            category_num = int(input("Please enter 1, 2, 3, 4 or 5  >>>  \n"))
            if 1 <= category_num <= 5:
                return category_num
            else:
                pass
        except ValueError:
            print("Only number 1, 2, 3, 4 or 5 accepted")


def select_question():
    """
    Random word selection from the list and display _ for each letter
    """
    time.sleep(2)
    category_chosen = category_select()
    list_num = category_chosen - 1
    print(f"Category {category_chosen}  was chosen")
    if category_chosen == 5:
        category_item = random.choice(category)
        word = random.choice(category_item)
        return(word)
    else:
        category_item = category[list_num]
        word = random.choice(category_item)
        return(word)


def hangman():
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
                    print(f"CONGRATULATIONS!"
                          f"You have guessed the word {word.upper()}.")
                    # ASCII ART https://patorjk.com/software/taag
                    print("██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗   ██╗")
                    print("██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝")
                    print("███████║██║   ██║██████╔╝██████╔╝███████║ ╚████╔╝")
                    print("██╔══██║██║   ██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝")
                    print("██║  ██║╚██████╔╝██║  ██║██║  ██║██║  ██║   ██║")
                    print("╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝\n")
                    break
                time.sleep(2)
        else:
            if len(guessed) > 1:
                print("Enter only one letter at a time")
            else:
                print(f"' {guessed.upper()}' is the incorrect answer!")

            incorrect += 1
            print("\n".join(stages[:incorrect]))
            print("\n")
            wrong_guess.append(guessed.upper())
            print(f"Your incorrect guesses: {wrong_guess} ")
            time.sleep(2)
    if incorrect == stage_num:
        print(f"The answer is {word.upper()}")
        game_over()

    time.sleep(3)
    replay()


def display_guess_message():
    print("\n")
    print("Can you guess the word?")
    print("Enter one letter to see if you are right?")


def display_alredy_used():
    print("You have already used this letter before,"
          " it's already displayed!")


def game_over():
    """
    GAME OVER ascii art
    """
    # ASCII ART https://patorjk.com/software/taag
    print(" _____ ____  _      _____   ____  _     _____ ____")
    print("/  __//  _ \/ \__/|/  __/  /  _ \/ \ |\/  __//  __\ ")
    print("| |  _| / \|| |\/|||  \    | / \|| | //|  \  |  \/|")
    print("| |_//| |-||| |  |||  /_   | \_/|| \// |  /_ |    /")
    print("\____\\_/ \|\_/  \|\____\  \____/\__/  \____\\_/\_\ ")


def replay():
    print("Would you like to play again?")
    print("Enter y or press RUN PROGRAM button above to play again.\n"
          "or press any other key to exit the game.")
    play_again = input(
        "Please press y to play, any other key to exit the game\n")
    if play_again.lower() == "y":
        hangman()
    else:
        print("Hope you enjoyed the game!")


def main():
    display_greeting()  # greeting function
    display_rules()  # display instruction if user chooses
    hangman()


main()
