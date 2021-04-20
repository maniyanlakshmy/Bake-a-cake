'''
This is the second level in the game. In this game, the player is prompted to enter a sentence. The sentence is converted into pi-latin and a random word is displayed.
The player is expected to match the converted word to the correct word from the sentence.
'''

import random                                           # random is imported
def piglat():                                           # The function piglat is defined
    consonants = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'   # The list of consonants is declared
    vowels = 'aAeEiIoOuU'                               # The list of vowels is declared
    print('\n P I G - L A T I N')
    while True:                                         # While the condition stays true
        piglatinwords = []                              # The list piglatinwords is declared
        print('\n Enter the sentence without punctuation and repetition :') # The player is prompted to enter a sentence
        inp = input()                                   # Input is obtained from the player
        inp = inp.split()                               # The sentence is converted into list of words

        for i in inp:                                   # The variable i is iterating inside the list inp
            if (i[0] in consonants):                    # If the word starts with a consonant
                pigchar = i[0]                          # The first character is removed and stored in pigchar
                pigword = i[1:]                         # The rest of the word is stored in pigword
                piglatin = pigword + pigchar + 'ay'     # piglatin is created by combining pigchar, pigword, and 'ay'
                piglatinwords.append(piglatin)          # piglatin is appended to the list piglatinwords
        for i in inp:                                   # The variable i is iterating inside the list inp
            if(i[0] in vowels):                         # If the word starts with a vowel
                piglatin = i + 'yay'                    # the suffix 'yay' is added along with the word
                piglatinwords.append(piglatin)          # The list piglatinwords is appended with the word piglatin
        randomword = random.choice(piglatinwords)       # A random word is selected from the list piglatinwords
        print('The word is :', randomword)              # The word is printed
        # The player is prompted to enter the matching word from the actual sentence
        print('\nThis word is given in piglatin. Type in the actual word from the sentence which you entered earlier :')
        inp1 = input()                                  # The entered word is stored in the variable inp1
        if(piglatinwords.index(randomword) == inp.index(inp1)): # The comparision is done by matching the index of the entered word and the randomword
            print('CONGRATULATIONS!!!! Eggs have been added to your inventory') # If the word matches the program proceeds further
            XP = 25                                     # The score is calculated to 25 XP
            return(XP)                                  # The value of the variable XP is returned
            break                                       # The program discontinues after this step
        else:                                           # If the entered word does not match the random word
            print('\nOH NO!! Wrong answer!! Try again') # The player is prompted to play again
            continue                                    # The program goes to the beginning of this module




