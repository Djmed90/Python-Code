# Darren Medeiros
# The program that I have made is the game Mastermind. What it does is generate a secret code (can use seed value) the person using this program
# has to guess the secret code based on he hints it is given a 1 meaning that the color (number) you chose is within the secret code or a  when the color (number)
# that you chose is equal to in position and color to the secret code.
# ------------------------------------------------------------------
# A couple of algorithms used:
# My first couple are my get secret algorithms that use inport randoma nd random.randint to use the seed given to generate random code to use for testing
# Then its the getGuess function and what it does is it takes your inputs and converts them to a string to then compare it in another function to the secret (there are many error handling cases in case you put something that the program is not loking for)
# Check guess for me was a big headache but able to figure out some indexing issues after a while. But in general check guess does what it says and compares both
# the secret to the guess to give you your clue. In it i made temp copies of the lists so i can pop already used numbers out.
# then the last 2 are the you guess that just is there to convert any guesses and secrets into their color counterpart list
# lastly is my first game and second game funciton that is the main function for the game i made two because when you restart i dont want it to use the seed value
# these games both keep track of guesses and have the checks for winning and losing
# lastly is the main fucntion that mostly contains the two games and asks if you want to play again

import random
ALL_COLORS = ['red','orange','yellow','green','blue','purple']

# Function that includes the seed to get the secret code
def getSecret(seedIn):
    secret = []
    for i in range(4):
        ln = random.randint(0,5)
        secret.append(ln)
    return secret
# Function that does not include the seed to get the secret code
def getSecret2():
    secret = []
    for i in range(4):
        ln = random.randint(0,5)
        secret.append(ln)
    return secret

# This Function gets the guess from the player 
def getGuess():
    print('-----------------------------')
    print('Make a guess of four colors:')
    print('0 - red')
    print('1 - orange')
    print('2 - yellow')
    print('3 - green')
    print('4 - blue')
    print('5 - purple')
    print('-----------------------------')
    guess = []
    for i in range(4):
        x = True
        # While this is true it will keep running this loop until the player inputs the correct notation
        while x == True:
            num = input(str('Guess color: '))
            # Tests if our variable num is not a numeric value if it is not numeric it prints a line then the continue sends you back to the start of while loop
            if not num.isnumeric():
                print('Invalid number, try again:')
                continue
            # This turns the string that you input into a number this is for case testing
            num = int(num)
            # If the Num is Greater than 5 you will get invalid guess and it will have you try again
            if num > 5:
                print('Invalid guess, try again:')
                continue
            x = False
        guess.append(num)
    return guess

# This function checks the guess taken from the player
def checkGuess(guess, secret):
    clue = []
    tempGuess = guess.copy()
    tempSecret = secret.copy()
    # It loops through 4 times and compares
    w = 0
    for i in range(len(secret)):
        # [1,3,3,3] secret
        if guess[i] == secret[i]:
            # If the secret and guess location are the same it appends a 2 to the list
            clue.append(2)
            if len(tempSecret) == 4:
                tempSecret.pop(i)
                tempGuess.pop(i)
            else:
                tempSecret.pop(i-w)
                tempGuess.pop(i-w)
            w = w + 1
    for i in range(len(tempGuess)):
        if tempGuess[i] in tempSecret:
            # If the guess location is not in the right spot but is in the secret list it will append a 1
            l = 0
            found = False
            while found == False and l < len(tempSecret):
                if tempGuess[i] == tempSecret[l]:
                    clue.append(1)
                    tempSecret.pop(l)
                    found = True
                l = l + 1
                    
    # This sorts the clue so that the player will not know exactly what they got right    
    clue.sort()
    return clue

# This function turns your guess into a word list to show after you put in your guess
def yourGuess(guess,secret):
    # Empty lists that are going to be used for howing the colors that are chosen
    defGuess = []
    defSecret = []
    # Loops through your guess list and appends the color to the defGuess list
    for i in range(len(guess)):
        j = guess[i]
        color = ALL_COLORS[j]
        defGuess.append(color)
    # Loops through your guess list and appends the color to the defSecret list
    for i in range(len(secret)):
        j = secret[i]
        color = ALL_COLORS[j]
        defSecret.append(color)
    return defGuess,defSecret

# Function for the First game that includes the seed
def firstGame(seedIn):
    # Uses the seed to get the random code
    random.seed(seedIn)
    x  = True
    winnerClue = [2,2,2,2]
    while x == True:
        win = False
        guesses = 0
        left = 10
        secret = getSecret(seedIn)
        print('The secret code has been chosen. You have 10 tries to guess the code.')
        # loop that loops each of your trys until you run out or its found
        while left != 0 and win == False:
            guess = getGuess()
            defGuess,defSecret = yourGuess(guess,secret)
            print('-----------------------------')
            print('Your guess is:')
            print(defGuess)
            clue = checkGuess(guess, secret)
            # If your guess wins you win! VV
            if clue == winnerClue:
                print('')
                print('Correct! You finished in ', guesses + 1, ' guesses')
                print('')
                return
            print('')
            print('Your clue is: ' , clue)
            print('')
            guesses = guesses + 1
            if left > 1:
                print('You have ', left - 1 , 'guesses left')
            left = left - 1
        print('No more guesses, the hidden colors were:')
        print('')
        print(defSecret)
        print('')
        return

# Function for the second game this is to enable restarting without having to get a seed
def secondGame():
    x  = True
    winnerClue = [2,2,2,2]
    while x == True:
        win = False
        guesses = 0
        left = 10
        secret = getSecret2()
        print('The secret code has been chosen. You have 10 tries to guess the code.')
        while left != 0 and win == False:
            guess = getGuess()
            defGuess,defSecret = yourGuess(guess,secret)
            print('-----------------------------')
            print('Your guess is:')
            print(defGuess)
            clue = checkGuess(guess, secret)
            # If your guess wins you win! VV
            if clue == winnerClue:
                print('')
                print('Correct! You finished in ', guesses + 1, ' guesses')
                print('')
                return
            print('')
            print('Your clue is:' , clue)
            print('')
            guesses = guesses + 1
            if left > 1:
                print('You have', left - 1 , 'guesses left')
            left = left - 1
        print('')
        print('')
        print('No more guesses, the hidden colors were:')
        print('')
        print(defSecret)
        print('')
        return
    
def main(seedIn):
    restart = True
    firstGame(seedIn)
    ok = True
    # loop that asks if you want to play again 'n' will end the program while 'y' will start a new one
    while ok == True:
        again = input(str('Would you like to play again? (Y/N)'))
        if again == 'Y' or again == 'N' or again == 'y' or again == 'n':
            ok = False
        else:
            print('Invalid')
            continue
        if again == 'N' or again == 'n':
            print('')
            print('Thank you for playing. Good-bye!')
            return 
        else:
            continue
    # This second game gets looped
    while restart == True:
        ok = True
        secondGame()
        while ok == True:
            again = input(str('Would you like to play again? (Y/N)'))
            if again == 'Y' or again == 'N' or again == 'y' or again == 'n':
                ok = False
            else:
                print('Invalid')
                continue
            if again == 'Y' or again == 'y':
                continue
            else:
                print('')
                print('Thank you for playing. Good-bye!')
                return
    return
