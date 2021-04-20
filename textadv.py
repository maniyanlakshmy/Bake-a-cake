'''
This program is designed to combine various word games that make use multiplt text manipulation techniques in a single platform.
This is a text-based adventure game. The player types in their answers when prompted and according to the given input, the game proceeds
There are four levels - meaning, four different games. The player has to complete all the four games successfully to finish this game.
'''
# importing the files
import game1ana, game2pila, game3hama, game4wosn
inventory = []                          # declaring a list "inventory" for storing prizes
score = 0                               # variable "score" is declared to tally the scores

#The following text is printed
print('\nWELCOME TO BAKE A CAKE \nThis is a text based adventure game.')
print('\nEarly morning. You wake up to the shrill cry of your alarm. With a groan, you pick up your mobile phone to switch it off')
print('\n You squint at the notification - It is your brothers birthday. And you have not done anything for the party')
print('\n You need to bake a cake. You need to hurry. ')

# This is the first level of the game
while True:                             # While the condition stays true
    print('\n You get out of your bed and look around. On the table, you see a packet of frosting. What do you do?(HINT : You can take the frosting or you can walk out of the room)')
    inp = input().lower()               # Input is obtained from the user and converted into lowercase

    if(inp == 'take the frosting'):     # If the input is "take the frosting"
        print('\nTo add the frosting to your inventory, you have to play a game. The name of the game is ANAGRAM!')
        print('\nThe rules of the game are : you have to enter five words, and you will be shown a scrambled version of those five words.')
        print('\n you have to identify which scrambled word matches which word you entered. You have to get at least three correct matches to proceed')
        score = game1ana.anagram()      # The function anagram from the file game1.ana is invoked - This is the first game
        inventory.append('Frosting')    # If the game is successfully completed, "Frosting" is added to the list
        break                           # If the game is successfully completed, the program proceeds to next level
    else:
        if(inp == 'walk out of the room'):   # If the given input is "walk out of the room"
            break                       # The program continues to the next level
        else:                           # If any other input is given
            print('Sorry, could you type it again?!')   # The text is printed
            continue                    # The program goes to the beginning promting the player to enter again

print("Score:", score)                  # The score is printed
print('Inventory :', inventory)         # The list - inventory is printed

# This is the second level of the game
while True:                             # While the condition stays true
    print('\nYou walk out into the hall. You spy a cupboard at the farther end of the hallway. Through the glass door, you see a carton of eggs')
    print('\n Let me remind you that you need eggs to bake the cake. What do you do?')
    print('\n(HINT: you can open the cupboard or go to the next room)')
    inp = input().lower()               # The player enters the input and is converted into lowercase

    if(inp == 'open the cupboard'):     # If the input is "open the cupboard"
        print('\nTo open the cupboard, you have to play a game. The name of the game is PIG LATIN!!')
        print('\nThe rules of the game are : you have to type in a sentence without punctuation.')
        print('\n A word will be displayed. This word is taken from your sentence, and you have to figure out which word it is!!')
        print('\n You have to get the correct answer to proceed!! Goodluck!!')
        scorepi = game2pila.piglat()    # The function piglat from the file game2pila is invoked - This is the second game
        score = score + scorepi         # The final score of the second game is added to the score of the first
        inventory.append('Eggs')        # The element "eggs" is added to the list "inventory"
        break                           # After successful completion the program continues to the next level
    else:
        if (inp == 'go to the next room'):  # If the given input is "go to the next room"
            break                       # The program continues to the next level
        else:                           # If any other input is given
            print('Sorry, could you enter again!?')
            continue                    # The program goes to the beginning of the second module

print("Score:", score)                  # The score is printed
print('Inventory :', inventory)         # The list inventory is printed

# This is the third level of the game
while True:                             # While the condition stays true
    print('\nYou go to your brothers bedroom. He has gone out. On the bed there is a big box of chocolates. You remember that chocolate is', end = "")
    print(' your brothers favorite flavour. \nLIGHTBULB!! You need the chocolate to make the cake. \nWhat do you do?(HINT : You can take the chocolate or you can go out of the room)')
    inp = input().lower()               # The input is obtained from the player and converted into lowercase
    if (inp =='take the chocolate'):    # If the input is "take the chocolate"
        print('To take the chocolate, you need to play a game! What game, you ask? The game is HANGMAN!!')
        print('\nThe rules are : A clue will be shown to you. Guess the word by entering the characters.')
        scorehm = game3hama.hangman()   # The function hangman from the file game3hama is invoked - This is the third game
        score = score + scorehm         # The score from the third game is added to the score variable
        inventory.append('Chocolate')   # The element "chocolate" is added to the inventory
        break                           # After successful completion, the program continues to the next level
    else:
        if (inp == 'go out of the room'):   # If the input is "go out of the room"
            break                       # The program continues to the next level
        else:                           # If any other inout is given
            print('Sorry, could you type it again!?')
            continue                    # The program goes to the beginning of the third module

print("Score:", score)                  # The score is printed
print('Inventory :', inventory)         # The list inventory is printed

# This is the fourth level of the game
while True:                             # If the condition stays true
    print('\nYou are on the staircase. You see a sack of flour on the ground. You need the flour for the cake. What do you do?')
    print('(HINT : You can pick up the flour or go to the groundfloor)')
    inp = input().lower()               # Input is obtained from the player and converted into lowercase
    if (inp == 'pick up the flour'):    # If the input is "pick up the flour"
        print('\n Like before, you need to play a game to complete this task. This game is called WORD-SNAKE!')
        print('\n The rules of the game is simple, you are supposed to enter words. The last letter of the first word should ', end =" ")
        print('match the first letter of the second word and so on. Good Luck!!')
        scorews = game4wosn.wordsnake() # The function wordsnake from the file game4wosn is invoked
        score = score + scorews         # The score of the fourth game is added to the previous scores
        inventory.append('Flour')       # The item "Flour" is added to the list inventory
        break                           # After successful completion, the program moves to the next level
    else:
        if (inp == 'go to the groundfloor'):    # If the input is "go to the groundfloor"
            break                       # The program goes to the next level
        else:                           # If any other input is given
            print('Sorry, could you enter it again?!')
            continue                    # the program goes to the beginning of the fourth module

print("Score:", score)                  # The score is printed
print('Inventory :', inventory)         # The inventory is printed

# This is the final stage of the game
print('\n You are now in the kitchen!')
if (score > 50) and (len(inventory) > 3):   # Checks whether the player has score above 50 and all the items in the inventory
    print('\nYou have', score, 'points and you have all the items to make the cake.')   # If the condition is satisfied, the player wins
    print('\nYou have won the game!!')
else:
    if(len(inventory) < 4):             # If the items in the inventory is less than 4, the player loses
        print('\nYou do not have the necessary items for making the cake. Play again!!')
    else:
        if (score < 45):                # If the score is less than 45, the player loses
            print('\nYou do not have enough score to make the cake. Play again!! ')





