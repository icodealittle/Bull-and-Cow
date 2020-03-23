'''
CS 5001
FALL 2019
Soumeng Chea
Programming 2

I consulted with TA's, classmates, and friends from other institute. 
'''

import random

def dup_digits(four_digits): #detect repetitive digits when player input digits....?????

    ''' Function: dup_digits
        Input: an integer list
        Return: boolean statement
        Do: Makes the list of integer into a set without any duplicate integers.
    '''

    four_digits = list(set(four_digits))
                       
    if len(four_digits) < 4:
        return False
    else:
        return True

def generator():
    ''' Function: generator
        Input: None
        Return: a list of integers
        Do: Run a for loop to produce secret four times with unique digits – the secret digits for the game
    '''
    # empty string will be filled with converted list of integers
    secret = []
    # random.sample returns a list of integers,
    # specify which numbers to choose between and specidfy length of list
    # range 0-9, specify the length of the list
    while len(secret) != 4:
        secret_num = random.randint(0, 9)
    # loop through the list of integers and change each element of the list into a string
    # save/append each string element to a string
        if secret_num not in secret:
            secret.append(secret_num)
        
    return secret

def user_player():
    '''Function: user_player
        Input:
        Return: the user input of 4-digit numbers
        Do: Prompt user to guess the secret digits. The function keep looping until the player statisfies the requirments.
    '''
    while True:
        player_guess = input('Enter 4 random numbers. Use space between them.   \n')
        player_guess = player_guess.split()

        if len(player_guess) != 4:
            print('TRY AGAIN! WITH JUST DIGITS')

        elif dup_digits(player_guess) == False:
            print('MUST BE UNIQUE!! NO REPEAT DIGITS!')

        else:
            count = 0
            for i in range(len(player_guess)):
                if player_guess[i].isdigit():
                    player_guess[i] = int(player_guess[i])
                    count += 1
                else:
                    print('MUST BE UNIQUE!! NO REPEAT DIGITS!')
                    break
            if count == len(player_guess): 
                return player_guess

def counts_bulls_and_cows(secret, player_guess): #main function of the game
    ''' Function: counts_bulls_and_cows
        Input: secret (a list of integers – generator function), player_guess (a list of integers – player_input)
        Return: Tuple of integers
        Do: Takes secret digits and input from the player to generate how many bulls and cows.
        
    '''
    
    bulls = 0
    cows = 0
    
    for i in range(len(secret)):
        if player_guess[i] == secret[i]:
            bulls += 1
        elif player_guess[i] in secret and player_guess[i] != secret[i]:
            cows += 1
            
    return bulls, cows




