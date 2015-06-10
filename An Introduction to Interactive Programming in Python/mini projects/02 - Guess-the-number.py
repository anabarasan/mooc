# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

limit = 100
secret_number = 0
remaining_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, limit)
    if limit == 100:
        remaining_guesses = 7
    elif limit == 1000:
        remaining_guesses = 10
    print ""
    print "New game. Range is from 0 to " + str(limit)
    print "Number of remaining guesses is " + str(remaining_guesses)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global limit
    limit = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global limit
    limit = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print ""
    print "Guess was " + guess
    guess = int(guess)
        
    global remaining_guesses
    remaining_guesses -= 1
    print "Number of remaining guesses is " + str(remaining_guesses)
    
    
    if guess > secret_number:
        result = "Higher!"
    elif guess < secret_number:
        result = "Lower!"
    elif guess == secret_number:
        result = "Correct!"
            
    if remaining_guesses > 0:
        print result
        if result == "Correct!":
            new_game()
    else:
        if result == "Correct!":
            print result
        else:
            print "You ran out of guesses.  The number was " + str(secret_number)
        new_game()
    
# create frame
f = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
range100 = f.add_button('Range 0 - 100', range100, 200)
range1000 = f.add_button('Range 0 - 1000', range1000, 200)
input_guess = f.add_input('Enter your Guess', input_guess, 200)

f.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
