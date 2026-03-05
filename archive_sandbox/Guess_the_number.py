import random
import os
        


#VARIABLES#
#1) Number variables
firstNumberRandom = random.randint(1, 10)
secondNumberRandom = random.randint(1, 50)
thirdNumberRandom = random.randint(1, 100)
#2) User variables
userDifficultyInput = 0
userGuessInput = 0
userAttempts = 5
isUserWon = False
#START#
print('\nHello! You have to choose difficulty, there are 3 levels:\n1.Easy (1-10)\n2.Medium (1-50)\n3.Hard (1-100).')

userDifficultyInput = int(input('Choose your difficulty (number): '))

if userDifficultyInput == 1 or userDifficultyInput == 2:
        while userAttempts != 0:
                os.system('cls')
                print('Attempts left: ' + str(userAttempts) + '\n\n')
                

                if userDifficultyInput == 1:

                        userGuessInput = int( input ('Ur guess (1-10): ') )


                        if userGuessInput == firstNumberRandom:
                                isUserWon == True
                                break
                        else:
                                print('Try again! *press any button to continue*')
                                input()

                elif userDifficultyInput == 2:
                        userAttempts = 15

                        userGuessInput = int( input('Ur guess (1-50):'))


                        if userGuessInput == secondNumberRandom:
                                isUserWon = True
                                break
                        else:
                                print('Try again! *press any button to continue*')
                                input()

                userAttempts = userAttempts - 1


elif userDifficultyInput == 3:
        os.system('cls')
        print('Phew! U choosed the hardest one! I\'ll let u to choose number of ur attempts for that difficulty!')
        userAttempts = int (input ('How many attempts u want to have in ur pocket? '))

        while userAttempts != 0:
                os.system('cls')
                print('Attempts left: ' + str(userAttempts) + '\n')
                
                
                        
                userGuessInput = int( input('Ur guess (1-100):'))


                if userGuessInput == secondNumberRandom:
                        isUserWon = True
                        break
                else:
                        print('Try again! *press any button to continue*')
                        input()

                userAttempts = userAttempts -1 

else: print('Error! Seems like something u wrote isn\'t right! Try again please ;)')


#RESULT PRINT#
if isUserWon == True:
        print('U\'ve beaten this this game! Congrats!')

elif isUserWon == False:
        print('Game OVER!')