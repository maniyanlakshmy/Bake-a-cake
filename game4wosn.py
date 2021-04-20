'''
This is the fourth level in the game. In this game, the player is prompted to enter 10 words. The first letter of the second word should
match with the last letter of the first word. Points are awarded based on the number of correct words entered
'''

def wordsnake():                                # The function wordsnake is defined
    fhand = open('wordlist.txt')                # A textfile containing a list of words in english is opened and stored in fhand
    wordlist = []                               # A list wordlist is declared
    inputwords = []                             # A list inputwords is declared
    for i in fhand:                             # The variable i iterates in fhand
        i = i.strip()                           # i is stripped of the space
        wordlist.append(i)                      # The value of i is appended into the list wordlist

    print('\nW O R D - S N A K E')
    print('Enter the word :')                   # The player is prompted to enter the first word
    inp = input()                               # The entered word is stored in the variable inp
    if inp in wordlist:                         # Checks whether inp is present in the wordlist
        inputwords.append(inp)                  # If inp is present in wordlist, inp is appended into inputwords
    else:                                       # If inp is not present in wordlist
        inputwords.append(inp)                  # inp is appended into the wordlist
        with open('wordlist.txt', "a") as fhandle:  # The textfile wordlist.txt is opened to update
            fhandle.write('%s\n' %inp)          # The word inp id added into the text file wordlist.txt
    count = 0                                   # A variable count is declared to be 0
    correctword = 0                             # A variable correctword is declared to be 0
    wrongword = 0                               # A varibale worngword id declared to be 0
    while (count < 9):                          # While the value of count is less than 9
        word = inputwords[count]                # The entered word is stored into the variable word
        print('Enter the next word:')           # The player is prompted to enter the next word
        inp1 = input()                          # The word is stored into the variabel inp1
        if inp1 not in wordlist:                # If the second word in not in wordlist
            with open('wordlist.txt', "a") as fhandle:  # The text file wordlist.txt is opened to update
                fhandle.write('%s\n' % inp1)    # The second word is added to the text fiel wordlist.txt
        if(word[-1] == inp1[0]):                # Checks whether the final letter of word and the first letter of inp1 is the same
            inputwords.append(inp1)             # If the condition is satisfied, the second word is appended to the inputwords
            correctword = correctword + 1       # The value of correctword is incremented by 1
        else:                                   # If the condition is not met
            # The player is prompted to try again
            print('The last letter of the first word does not match with the first letter of this word. Try again')
            wrongword = wrongword + 1           # The variable wrongword is incremented by 1
            continue                            # The program goes to the beginning
        count = count + 1                       # The value of countis increased by 1

    if (correctword == 10) or (correctword > 10):           # If correctword is greater than or equal to 10
        print('Flour has been added to your inventory')
        XP = 25                                             # The score is 25
        return(XP)                                          # The score is returned
    if (correctword > 7) and (correctword < 10):            # If correctword is greater than 7 and less than 10
        print('Flour has been added to your inventory')
        XP = 20                                             # The score is 20
        return(XP)                                          # The score is returned
    if (correctword > 4) and (correctword < 7):             # If correctword is greater than 4 and less than 7
        print('Flour has been added to your inventory')
        XP = 15                                             # The score is 15
        return(XP)                                          # The score is returned
    if (wrongword == 10):                                    # If wrongword is greater than or equal to 10
        print('Since you scored zero, Flour was not added to your inventory.')
        XP = 0                                              # The score is 0
        return(XP)                                          # The score is returned




