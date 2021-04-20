'''
This is the third level in the game. In this game, the player is given a clue and they are supposed to guess a word. 10 chances are given,
and as they enter the letters, it will get added to the appropriate space
'''

import random, re                                   # Random and re are imported

def hangman():                                      # The function hangman is defined
    print('\nH A N G M A N')
    # A dictionary containing key as the words and the values as the clues is declared
    wordlist = {'RAINBOW':'Colours on the sky', 'THUNDER':'I was lightning, before this', 'LEVIOSA':'Wingardium', 'LORD':'Of The Rings', 'CHAMBER':'Harry Potter and ___ of Secrets'}
    rand = random.choice(list(wordlist.items()))   # A random item from the dictionary is chosen and stored into rand
    rand = list(rand)                               # The variable rand is converted into list

    print('The clue is :', rand[1])                 # The clue, that is the second element in the list rand is displayed
    blanks = '_ '*len(rand[0])                      # The corresponding word is displayed as blanks with the same lenth
    print(blanks)

    word = []                                       # A list word is declared
    turn = 10                                       # The variable turn is declared with the value 10
    count = 0                                       # The variale count is declared to be 0
    while turn > 0:                                 # While the variable turn is greater than 0
        print('\nGuess the word. Enter the characters below. (Enter in Capital letters) ')  # The player is prompted to enter a letter
        inp = input()                               # The letter is stored in the variable inp

        if inp == rand[0]:                          # If the player is able to guess the word correctly, the program is discontinued and the player is awarded full points
            print('WOW!! You got the right answer!! Chocolate has been added to your inventory!!')
            break                                   # The program is discontinued
        else:                                       # If the player enters a character
            if inp in rand[0]:                      # If the input character is in the 1st element of rand
                index = rand[0].index(inp)          # The index of the input character is stored in to the variable index
                blanks = blanks[:index] + inp + blanks[index+1:]    # The input character is entered in to the blanks
                print(blanks)                       # The word is printed
                temp = blanks.replace('_','')       # The "_" in the variable balnks is replaced with empty spaces
                res = re.sub(' +', '', temp)        # The extra spaces are removed using Regular expressions
                output = str(res)                   # The variable res is converted into string
                if (sorted(output) == sorted(rand[0])): # The comparison done by sorting the variable output and rand[0]
                    print('Congratulations! You have found the word. Chocolate has been added to your inventory')
                    print('Number of chances left :', turn) # If the words match, the player is awarded points according to the turns
                    break                           # The program is continued
            else:                                   # If the entered character is not in the random word
                print('The character is not in the word:')
                print('You have', turn, 'chances left') # The player is prompted to play again
                continue                            # The program goes to the beginning of the module
        turn = turn - 1                             # The variable turn is decreased by one
        if turn == 0:                               # When the value of turn becomes zero
            print('Sorry, you will have to try again')  # The player is prompted to try again
            continue                                # The program goes to the beginning of the module

    if turn == 10:                                  # If the value of turn is 10, i.e, if the player has guessed the word in the first try,
        XP = 25                                     # The score is 25
        return(XP)                                  # The score is returned
    if (turn < 10) and (turn > 3):                  # If the value of turns is between 3 and 10
        XP = 20                                     # The score is 20
        return(XP)                                  # The score is returned

