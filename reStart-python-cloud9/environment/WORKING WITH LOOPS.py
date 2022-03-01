import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True: #If the user has not guessed the correct answer, enter the loop.
    guess = input("Guess a number between 1 and 10: ") # Ask the user for a guess.
    if int(guess) == number: #Is the guess the correct number?
        print("You guessed {}. That is correct! You win!".format(guess)) #If the correct guess, tell the user it was the correct guess and exit the loop.
        isGuessRight = True 
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess)) #If the wrong guess, tell the user it was the wrong guess and continue the loop.
        
        