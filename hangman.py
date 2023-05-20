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
    print('Guess the word! HINT: Word is a name of a fruit')

    for i in word:
        print('_', end = ' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
                print()
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER!')
                continue

            elif len(guess) > 1:
                print('Enter Only a SINGLE Letter!')
                continue

            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

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
        
        if (chances <= 0) and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You Lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
