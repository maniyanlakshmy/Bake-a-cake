'''
This is the first level in the game. In this game, the player is prompted to enter five words. These words are scrambled, and again their order is also changed.
The player is expected to match the actual words to the scrambled words. Points are awarded based on how many correct words are matched
'''

from random import shuffle, sample              # shuffle and sample are imported from random
def anagram():                                  # The function anagram is defined
    print('\nA N A G R A M')

    while True:                                 # While the condition is true
        inputwords = []                         # The list inputwords is declared
        outputwords = []                        # The list outputwords is declared
        newoutputwords = []                     # The list newoutputwords is declared
        tally = 0                               # The variable tally is declared
        XP = 0                                  # The variable XP is declared
        print('Enter five words :')             # The player is prompted to enter five words
        count = 0                               # The variable count is declared
        while(count<5):                         # While count is less than 5
            inp = input()                       # The player enters the word
            inputwords.append(inp)              # The words are appended to the list inputwords
            count = count+1                     # count is increased by 1

        for i in inputwords:                    # The variable i is iterated within the list inputwords
            inp = list(i)                       # The word i is converted to list
            shuffle(inp)                        # The characters of i is shuffled
            anagram = ''.join(inp)              # The scrambled characters are joined and stored in the variable anagram
            outputwords.append(anagram)         # The scrambled word is appended to the list outputwords
        newoutputwords = sample(outputwords, len(outputwords))  # The list outputwords is scrambled and stored in the list newoutputwords
        print('The scrambled words are :')
        print(newoutputwords)                   # The scrambled list is printed
        print('\n Now, match the words :')

        count1 = 0                              # New variable count1 is declared
        while(count1 < 5):                      # While count1 is less than 5
            # Player is prompted to enter the number corresponding to the matching word
            print('\n For the', (count1+1), 'scrambled word, what is the number of the word in your list (Hint : 0 is the first word, 4 is the last word) ?')
            wordnum = input()                   # Input is obtained from the player and stored into variable wordnum
            wordnum = int(wordnum)              # The variable wordnum is converted into integer
            if(sorted(inputwords[wordnum]) == sorted(newoutputwords[count1])):  # Comparison is done by sorting the scrambled word and the matched word. If they are the same,
                tally = tally + 1               # The variable tally is increased by 1
                XP = XP + 5                     # The variable XP is increased by 5
            count1 = count1 + 1                 # The variable count1 is increased by 1

        print('You got a total of ', tally, 'correct answers!') # The final count of correct answers is printed
        print('Your score is ', XP, 'XP')       # The score is printed

        if (tally > 3) or (tally == 3):         # If the number of correct answers is greater than or equal to 3
            print('\nCONGRATULATIONS!!! Frosting is added to your inventory')
            return(XP)                          # The score is returned
            break                               # The program is stopped
        else:                                   # If the score is less than 3
            print('You did not get enough points to clear this level. PLAY AGAIN!!!')
            continue                            # The program goes to the beginning of the module. The player has to play again.

