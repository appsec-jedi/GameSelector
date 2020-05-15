"""
Simple game selector project
"""

import random
import array

#show the game selection and start the game
def game_selector(choice):
    if choice == "1":
        print("\nOK! Let's play Rock Paper Scissors!")
        rock_paper_scissors()
    elif choice == "2":
        print("OK! Let's play Hangman")
        hangman()
    else:
        print("Sorry, I don't know that one")

#rock paper scissors game
def rock_paper_scissors():
    #take in user choice 
    user_choice = input("\nMake your selection: ") 
    
    #randomly select a number between 1 and 3 for the computer choice and determine game outcome
    computer_choice = random.randint(1,3)
    if user_choice.lower() == "rock":
        if computer_choice == 1:
            print("Computer chose rock. It's a tie!")
        elif computer_choice == 2:
            print("Computer chose paper. You lose!")
        elif computer_choice == 3:
            print("Computer chose scissors. You win!")
    elif user_choice.lower() == "paper":
        if computer_choice == 1:
            print("Computer chose rock. You win!")
        elif computer_choice == 2:
            print("Computer chose paper. It's a tie!")
        elif computer_choice == 3:
            print("Computer chose scissors. You lose!")
    elif user_choice.lower() == "scissors":
        if computer_choice == 1:
            print("Computer chose rock. You lose!")
        elif computer_choice == 2:
            print("Computer chose paper. You win!")
        elif computer_choice == 3:
            print("Computer chose scissors. It's a tie!")
    else:
        print("Invalid selection")
    one_more_time()

#start hangman
def hangman():   
    
    #randomly select one of four words
    word_chooser = random.randint(1,4)
    if word_chooser == 1:
        word_choice = "auburn"
    elif word_chooser == 2:
        word_choice = "cloud"
    elif word_chooser == 3:
        word_choice = "security"
    elif word_chooser == 4:
        word_choice = "pineapple"

    #moving the chosen word into an array and creating an empty array to display missing and chosen characters
    display_word_array = [None] * len(word_choice)

    #setting values for characters remaining to be guessed and turns remaining 
    remaining_characters = len(word_choice)
    turns_remaining = 10

    #variable to hold already guessed letters
    already_guessed = ""

    #create and display the blanks for the word
    word_length = len(word_choice)
    array_index = 0
    while True:
        display_word_array[array_index] = "_ "
        word_length = word_length - 1
        array_index = array_index + 1
        if word_length == 0:
            break
    
    #function for information to display including turns remaining, characters guessed and the missing blanks
    def display_module():
            print("\nYou have ", turns_remaining, " guesses remaining.")
            print("\nAleady guessed letters: ", already_guessed)
            for char in display_word_array:
                print(char, end ="")

    display_module()

    #taking in user input and comparing to the selected word
    while True:
        user_guess = input("\nWhat's your guess?: ").lower()
        turns_remaining = turns_remaining - 1
        letter_found = False
        index = -1
        for char in word_choice:
            index = index + 1
            if char == user_guess:
                #index = word_choice.index(user_guess)
                display_word_array[index] = user_guess
                remaining_characters = remaining_characters - 1
                letter_found = True

        #if the letter isn't found in the selected word, tell the user and add the letter to the already_guessed string
        if letter_found == False:
            already_guessed += user_guess
            print("\nSorry, pick again")

        #if the remaining character reaches zero, the user wins!
        if remaining_characters == 0:
            print("\nCorrect! The word was ", word_choice)
            print("\nYou win!\n")
            one_more_time()
            break
        
        #if turns remaining reaches zero, the user loses
        elif turns_remaining == 0:
            print("\nBetter luck next time!\n")
            one_more_time()
            break
            
        #displaying the mode
        display_module()
        

def want_to_play():
    #take in user input
    print("\nHey friend, do you want to play a game? ")
    play = input("Enter Yes or No ").lower()

    #get user selection for the game
    if play == "yes" or play == "y":
        print("\nWhich one would you like to play?\n1) Rock Paper Scissors\n2) Hangman")
        game_choice = input("\nEnter the number for the game you'd like to play: ")
        game_selector(game_choice)
    elif play == "no" or play == "n":
        print("I'm sorry you don't want to play\nCome back soon!")
    else:
        print("Sorry, I didn't catch that")
    

def one_more_time():
    play_again = input("\nWould you like to play another game? ").lower()
    if play_again == "yes" or play_again == "y":
        print("\nLet's do it!")
        print("\nWhich one would you like to play?\n1) Rock Paper Scissors\n2) Hangman")
        game_choice = input("\nEnter the number for the game you'd like to play: ")
        game_selector(game_choice)
    elif play_again == "no" or play_again =="n":
        print("\nI didn't want to play anyway. Bye!")
    else:
        print("Sorry, I didn't catch that")

#start the program
want_to_play()

