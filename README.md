# HANGMAN game

Hangman game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

# How to play

# Features

### Exsisting Features

### Future Features

# Data Model

# Testing

I have manually tested this project by doing the following:
* Passed the code through a PEP8 linter and confirmed, there are no problems
* Give invalid inputs strings when numbers are expected, out of bound inputs, some inputs twice
* Tested in my local terminal and the Code Institute Heroku terminal

## Bugs

### Solved Bugs

## Remaining Bugs

* No bugs remaining

## Validator Testings

* PEP8 http://pep8online.com/checkresult
    * No errors were returned from PEP8online.com

# Deployment

# Credits

* Code Institute for the deployment terminal
* 
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!