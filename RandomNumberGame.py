# AAI/CPE/EE 551 Section WS Engineering Programming: Python Spring 2022 Final-project
# Name: Pratik Patil
# CWID: 10477825
#==============================================================================

# This is my Random Number Guessing Game project


import random

def gamePlay(chances, guess, secret, num):
    count = 1                                                                   # Initialize a counter to limit the chances asked by user
    def guessNumGeneratorValidator():                                           # Inner function to ask guess number from user                                      
        status= True                                                            # Set a status flag as TRUE
        while status:
            newNum = input ('Please type a number between 1 and ' + str (num) + ": ")
            if newNum.isdigit():
                newNum = int (newNum)
                if newNum <=num and newNum>=1:
                    status = False
                else:
                    print('Input Value is out of range :( Please input a value within mentioned range !!!')
            else:
                print ('Invalid input! Try Again!')
        return newNum
        
    while guess != secret:
        guess=guessNumGeneratorValidator()                                      # new valid guessed number by user is stored in "guess" variable
        
        if guess == secret:                                                     # Base Condition of guessing success
            print ('              ############ YOU GOT IT!!! ############')
            if count==1:                                                        # condition for special message
                return "Congratulations!!! It took you just "+str(count)+" chance to guess the right number :-)"
            else:
                return "It took you "+ str(count) +" chances to guess the right number!!!"
        else:
            print("Chance : ",count)
            if guess<secret:                                                    # condition is used to give a user hint for next better guess
                prompt="You guessed SMALLER than the secret number";            # Default message
                if guess in range(secret-3,secret+1):                           # If guess is so close to secret number condition
                    prompt+= " AND you are SO CLOSE to your secret number";     # Additional hint message is concatenated to the default message
                print("**HINT : "+prompt)
            elif guess>secret:                                                  # condition is used to give a user hint for next better guess
                prompt="You guessed LARGER than the secret number";             # Default message
                if guess in range(secret,secret+4):                             # If guess is so close to secret number condition
                    prompt+= " AND you are SO CLOSE to your secret number";     # Additional hint message is concatenated to the default message 
                print("**HINT : "+ prompt)
            count+=1
            if count-1 == chances:                                              # Conditional statement to stop playing wheb user used all chances to guess the number
                return "Sorry, Your chances are Over !!!"  

            print ('Please try again!'+'\n')                                    # Default message after every wrong guess



# Program Starts from Here
if __name__ == "__main__":
    print("====== Welcome To Random Number Guessing Game !!! ======")
    while True:                                                                 # While condition for continuously keep playing new game until user enters any other key except 'Y'
        # This loop is for designing a Start Play Button
        for i in range(0, 4):
            for j in range(0, i + 1):
                print("*", end=' ')
            print("")
        print("S T A R T")
        for i in range(5, 0, -1):
            for j in range(0, i - 1):
                print("*", end=' ')
            print("")
        
        # Below While loop is used for recursivlely checking for Valid Integer Inputs
        flag = True                                                             # Set flag as TRUE
        while flag:
            num = input ('Please input number for higher limit of your game (value should be greater than one): ')
            if num.isdigit():
                num = int (num)
                if num>1:                                                       # Checking the value of higher limit as we started our random number from 1
                    flag = False
                else:
                    print ('Please give a input value greater than one!!!')
            else:
                print ('Invalid input! Try Again!')

        # Below While loop is used for recursivlely checking for Valid Integer Inputs
        chanceflag = True                                                       # Set flag as TRUE
        while chanceflag:
            chances = input ('Please input number, In How many chances do you want to guess the secret number? : ')
            if chances.isdigit():
                chances = int (chances)
                if chances>=1:
                    print ("                           Let's Play!!!                        ")
                    chanceflag = False
                else:
                    print ('Invalid input! You should play with at least 1 chance!!!')
            else:
                print ('Invalid input! Try Again!'+'\n')
                
        # Creating a secret random number
        secret = random.randint (1,num)                                         # set a secret value
        print("********************* Secret Key is generated *********************")
        guess = None                                                            # Initialize guess value to None
        
        output=gamePlay(chances, guess, secret, num)                            # gamePlay() function called and returned value stored in variable for future use
        
        # Conditional statement to check whether user wants to continue playing or not 
        if output=="Sorry, Your chances are Over !!!":
            print('\n'+output+' Better Luck Next Time :-)'+'\n'+'==========================================================================================='+'\n')
            
            ask=input("Do you want to play again? Type Y to play again OR press ANY other key to Stop the Game: ")
            if ask=='Y':continue                                                # if user input is 'Y' then, Again Start the code from begining
            else:
                print("Thank You for playing!!!")
                break                                                           # Stop code at any other key press than 'Y' 
        else:
            print(output+'\n'+'==========================================================================================='+'\n')
            ask=input("Do you want to play again? Type Y to play again OR press ANY other key to Stop the Game: ")
            if ask=='Y':continue                                                # if user input is 'Y' then, Again Start the code from begining
            else:
                print("Thank You for playing!!!")
                break                                                           # Stop code at any other key press than 'Y'


#====================================== THANK YOU !!! Happy Gaming!!! ========================================