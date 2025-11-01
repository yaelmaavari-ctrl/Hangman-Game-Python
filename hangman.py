import random
from multiprocessing.connection import answer_challenge
from operator import index, truediv

HANGMANPICS = [r'''

  +---+
  |   |
      |
      |
      |
      |
=========''', r'''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#======כאן יש להוסיף אוסף של מילים=====

words=['hello','yael','banana','apple','child']

#============כאן יכתבו הפונקציות=============
def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)] )
    print('missedLetters: ' +missedLetters)
    print('correctLetters: '+correctLetters)
    print(currentWord)


def getGuess(alreadyGuessed):
    g=input("enter a new guess")
    if (g in alreadyGuessed or g=="" or len(g)!=1 or not g.isalpha()):
        print("invalid letter")
        return getGuess(alreadyGuessed)
    else:
        return g

def playAgain():
    answer=input("do you want to play again?  ")
    if answer=='yes':
        return True
    elif answer=='no':
        return False
    else:
        print("invalid answer")
        return playAgain()

#========כאן תחילת המשחק================

missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = words[random.randint(0,len(words)-1)] #לרנדם מילה
currentWord= len(secretWord)*'_'
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # המשתמש מקיש אות ובודקים אם זה תקין
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        currentWordList=list(currentWord)
        for i in range(len(secretWord)):
            if(secretWord[i]==guess):
                currentWordList[i]=guess
        currentWord=''.join(currentWordList)
        print(currentWord)
    else:
         missedLetters=missedLetters+guess

        #בדיקה אם השחקן ניצח
    foundAllLetters = True
    for l in range(len(secretWord)):
         if secretWord[l] not in correctLetters:
            foundAllLetters = False
            break
    if foundAllLetters:
        print('Yes! The secret word is "' + secretWord + '"! You have won!')
        gameIsDone = True

        # בדיקה האם השחקן הפסיד
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # האם השחקן רוצה לשחק שוב??
	#אתחול המשתנים והמשחק מתחדש...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = words[random.randint(0,len(words)-1)] #לרנדם מילה
            currentWord= len(secretWord)*'_'
            continue
        else:
            break