# Python program to make a hangman game

# Importing random and counter libraries here
import random
from collections import Counter

# This contains our words. You can add more words if you want but just make sure each word have a space between them
# You can add your own words, like Movie names, Sport names... Sky is the limit here
someWords = ''' apple banana lemon melon cherry pineapple'''

# This splits our words into list, like this [apple, banana, lemon (and so on until all our words are here)]
someWords = someWords.split(' ')

# Here we have use our random function where it chooses any words from above randomly. Even I don't which word is selected here.
word = random.choice(someWords)


# Here our main program starts runnnig
if __name__ == '__main__':

    # This statement below prints the first message for the user.
    print('Guess the word! HINT: Word is a name of a fruit')

    # This line below prints the empty spaces of the word chosen in 'word' variable
    for i in word:
        print('_', end = ' ')
    print()                           # This line is used as to skip this whole line or line break as in html

    # User is playing until he has all the chances. This flag is true but if all chances are gone this flag goes to false
    playing = True

    # This variable is used to store the correctly guessed ABC characters that the user guessed
    letterGuessed = ''

    # This here gives the number of chances depends on the number of word a words has and plus two
    chances = len(word) + 2

    # This flag is 0 initially and its used if the word is correctly guess then correct changes to 1 thus ending the game
    correct = 0

    # This flag is used to check if tha game is still going on or stopped. If the user wins the game, this flag changes to 1 -
    # - thus ending the game.
    flag = 0

    # Using try statement to start our game logic
    try:

        # Using While statement here to run the game until all chances are zero or flag is 1
        while (chances != 0) and flag == 0:

            # This line is used as line break just like in html
            print()

            # Chances is lowered by one or subtracted by one
            chances -= 1

            # Try statement here to get the input from the user
            try:
                guess = str(input('Enter a letter to guess: '))
                print()
            
            # Except statement will run if there is no input from the User
            except:
                print('Enter only a letter!')
                continue

            # Here we are validating that the input user have given us is valid or no
            if not guess.isalpha():
                print('Enter only a LETTER!')
                continue

            # Here we are validating that the input user have given us is more than one because we only need one letter
            elif len(guess) > 1:
                print('Enter Only a SINGLE Letter!')
                continue

            # Here we are validating that the input user have given us is already guessed or no
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # After passing through all the validation above, the input is stored in a letterGuessed variable
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            # Then we use for loop for each word, if the word is correct it prints out the word otherwise a blank space
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                
                elif (Counter(letterGuessed) == Counter(word)):
                    print('The word is', end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                    break
                else:
                    print('_', end=' ')
            print()
        
        # If the player has used all the chances and still did not get the word right, this below logic will run
        if (chances <= 0) and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You Lost! Try again..')
            print('The word was {}'.format(word))
    
    # If you want to exit the game, just press "Ctrl + C" on windows. For other operating system, kindly google it.
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
