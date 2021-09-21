# HANGMAN game

This game ws built as part of the learning material for Code Institute's Fullstack Web Developer program (5P) Portfolio Project.

Portfolio Project Three: Python - Code Institute - Deadline 24th September 2021

Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words Python terminal game, which runs in the Code Institute mock terminal on Heroku.

You can check out the live game [here](https://hangman-game1x.herokuapp.com/)

![my-page](controllers/assets/images/my-app-image.png)


# Table of Contents

* How to play

* Features
   * images
   * future features

* Data model

* Technology

* Testing
   * Bugs
   * Validator testing

* Deployment

* Credits


# How to play

* If you know how to play the game you can start the game, otherwise you can read about how to play the game.

* You will have to make a choice on which category to select

* You will be presented with a number of blank spaces representing the missing letters you need to find.

* Use the keyboard to guess a letter (I recommend starting with vowels).

* If your chosen letter exists in the answer, then all places in the answer where that letter appears will be revealed.

* After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.

* Every time you guess a letter wrong you lose a life and the hangman begins to appear, piece by piece.

* To win you need to solve the puzzle before the hangman dies.

# Features

### Exsisting Features (with functions)

![game start](controllers/assets/images/heroku-start-game.png)

![game-start](controllers/assets/images/heroku-start-welcome.png)

   * Display greeting , ASCKII art, user input for name 
      * def display_greeting()

![game rules](controllers/assets/images/game-rules.png)
 
   * Ask the player either display the rules or go for game
      * def display_rules()
   * Display rules
      * def rules_txt()

![game categories](controllers/assets/images/heroku-category.png)

   * Display categories
   * User input for selecting category  
      * def category_select()

![letters joice](controllers/assets/images/heroku-incorrect-right-letter.png)

![end image](controllers/assets/images/heroku-end-lost.png)

   * Ask the player to enter letters one at the time
   * if the player entered a letter which is right for the randomly selected word,
      the letter will be displayed instead of "_" underscore
   * if the player enters a letter which is not in the word, the hangman image starts to 
      develop
   * the player gets a note when double selected the same letter  
      * def select_question()   
      * def hangman()
      * def display_guess_message()
      * def display_alredy_used()

![hurray](controllers/assets/images/heroku-end-winning.png)   

   * If user guessed all letters, display ASCII image - Hurray!  
      * def hangman()

![game over](controllers/assets/images/game-over.png)  
   * end of game display image ASCII art 
   * ask the player would he like to play again or exit the game using keybord or Run Programm button above
   * user input what choice he made  
      * def game_over()
      * def replay()


### IMAGES   

Are created by using [ASCII art](http://patorjk.com/software/taag)

![hangman greeting](controllers/assets/images/hangman-image.png)

![hurray](controllers/assets/images/hurray-image.png)

![game over](controllers/assets/images/game-over-image.png)

Visual [hangman stages](https://enhancer298.net/2020/07/10/hangman1/)

![hangman stages](controllers/assets/images/hangman.png)



### Future Features


* The hangman game is an old, old game and seeing the games title as a childrens game can be odd. Taking into consideration mental health and suitside issues. So for that reason I would like to give different visualisation options where you can select build a snowman or melting snowman.

* more categorys to select

* bigger list of words. Special file to accomodate that.

* for a language learning purpose iy would be good to hear the words sound.

* the letters can be displayed for selection

* different difficulty levels 


# Data Model

This is the flowchart made during the planning stage of the project. This flowchart has been used to visualise the functions and behaviour control during the building stage of the project.

<details><summary>Flowchart</summary>

![Flowchart](controllers/assets/images/hangman-flowchart.jpeg)
</details>


# Technology


*  This game was created with:

    * [Gitpod](https://www.gitpod.io/) used to develop project and organise version control 

    * [Github](https://github.com) used to host repository
       
    * [Heroku](https://id.heroku.com/login) used to deploy my application

* [Lucid](https://lucid.app/users/login#/login) used to create the flowchart for the project.

* [Grammarly](https://app.grammarly.com/) used to fix the thousands of grammar errors across the project.

* The Code Institute's GitHub full template for Python is used in order for the program to display properly in the deployed site on Heroku.

* [random](https://docs.python.org/3/library/random.html) to randomize anagram

* [time](https://docs.python.org/3/library/time.html) to slow down printed statements

* Python 3 - an interpreted high-level general-purpose backend programming language.

# Testing


I have manually tested this project by doing the following: 
* Passed the code through a PEP8 linter and confirmed, there are no problems (find under validator testing)
* Give invalid inputs strings when numbers are expected, out of bound inputs, some inputs twice

<details><summary>Only numbers</summary>

![only numbers](controllers/assets/images/only-numbers.png)
</details>

<details><summary>Tested ASCII art printout</summary> 

![ascii](controllers/assets/images/test-greeting-print.png)
</details>

* Tested in my local terminal and the Code Institute Heroku terminal
* [Python tutor](https://pythontutor.com/visualize.html#mode=edit)

<details><summary>Test sample</summary>

![python-tutor](controllers/assets/images/pythontutor-image.png)
</details>

<details><summary>Lighthouse</summary>

![lighthouse](controllers/assets/images/lighthouse-hangman.png)
</details>

## Bugs

### Solved Bugs


* Heroku, the deployment terminal was set to 80 colums and 24 rows.

At first I was just writing lines and after error showing fixed line lenght.

* ASCII art gave lots of white space, what needed to be fixed by deleting them. 

I selected for every image different font. Block element font was easy to fix.

Image "Game over" is created using line art and it was impossible to solve 
* errors
   * flake8(W605)
   * plynt(anomalous-blacklash-in-string)

* I used manual deployment to get to know more deployment process for study purpose.

I forgot fresh deployment when I asked someone to play and they reflected things
what I already fixed or changed.So time by time I was confused why in gitpod terminal 
evrything works well but not in Heroku. Im glad I chosed manual deployment. 

* I used + name + for print out greeting and name but it didnt separate "name" from rest of the text.
   * used print(f"Hello {name.upper()}, Best of luck!") gave me result what I wanted.

* Spelling mistakes can give you headach but I know my weaknes. 
   * Patience to go over your lines gives results

* By accidentally I deleted two times my all run.py coding. Very scary experience
   * During my second project I went to Github and copied code from there. Lucky if its saved...
   * Used Ctrl + Z this time. 

## Remaining Bugs

* No bugs remaining

## Validator Testings

* [PEP8](http://pep8online.com/checkresult)
    * No errors were returned from PEP8online.com

<details><summary>PEP8 validator testing</summary>

![pep8](controllers/assets/images/pep8online.png) 
</details>   

# Deployment


This project was deployed using Code Institute's mock terminal for Heroku. Please follow the below steps.

## Deployment steps

1. Git add and git commit the changes made

2. Log into [Heroku](https://id.heroku.com/login) or create a new account and log in

3. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

4. Write app name - it has to be unique, it cannot be the same as this app

5. Choose Region - I am in Europe

6. Click "Create App" The page of your project opens.

7.  Choose "settings" from the menu on the top of the page

8. Go to section "Config Vars" and click button "Reveal Config Vars"

<details><summary>Click to see it</summary>

![config vars](controllers/assets/images/config-vars.png)
</details>

9. In the field for "KEY" enter "PORT"-  capital letters and value"8000" 

10. Go to section "Build packs" and click "Add build pack"

   * in this new window - click Python and "Save changes" [`heroku/Python`]
   * click "Add build pack" again
   * in this new window - click Node.js and "Save changes" [`heroku/NodeJS`]
   * take care to have those apps in this order: [`Python`] first, [`Node.js`] second, drag and drop if needed

<details><summary>Click to see it</summary>

![buildpacks](controllers/assets/images/buildpacks.png)
</details>

11. Next go to "Deploy" in the menu bar on the top

12. Go to section "deployment method", choose "GitHub"

13. New section will appear "Connect to GitHub" - Search for the repository to connect to

14. type the name of your repository and click "search"

15. once Heroku finds your repository - click "connect"

16. Scroll down to the section "Automatic Deploys"

17. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy
   * As I wanted to have control when to deploy the version, I have chosen manual deployment by pressing Deploy branch button instead of Enable Automatic Deploys

<details><summary>Click to see it</summary>

![deployment](controllers/assets/images/manual-deployment.png) 
</details>  

18. Click "Deploy branch"

Once the program runs: you should see the message "the app was sussesfully deployed"

<details><summary>Click to see it</summary>

![deployed](controllers/assets/images/heroku-app.png)
</details>

 19. Click the button "View". This View button will open the terminal game in the new window. Here is the deployed page [Hangman](https://hangman-game1x.herokuapp.com/)

 20. As manual deployment was chosen, I had to come back to Heroku deployment page whenever I have an updated working version pushed into the GitHub page.

# Forking the GitHub repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log into [GitHub](https://github.com/) or [create an account](https://github.com/).

2. Locate the GitHub repository. Link can be found [here](https://github.com/HeleJ/hangman-game).

3. At the top of the repository, on the right side of the page, select "Fork".

4. You should now have a copy of the original repository in your GitHub account.

# Making a local clone

1. Locate the GitHub repository. Link can be found [here](https://github.com/HeleJ/hangman-game).

2. Next to the green Gitpod button you will see a button "code" with an arrow pointing down

3. You are given the option to open with GitHub desktop or download zip

4. You can also copy https full link, go to git bash and write git clone and paste the full link

# Credits

* Code Institute for the deployment terminal

* To create the game I got help [from](http://inventwithpython.com/invent4thed/chapter8.html)

* Idea for [flowchart](http://inventwithpython.com/invent4thed/chapter7.html)

* John at CI Tutor support for his patience and pointing me into the right direction.

* Kasia at CI, our group leader. Amazing teacher, who gives more than 100% to get us true. Thanks to her Im still studying in this course. Thanks to her Im finishing my third project.

