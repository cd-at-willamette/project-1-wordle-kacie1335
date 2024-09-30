########################################
# Name: Kassandra Carrasco
# Collaborators (if any):QUAD Center
# GenAI Transcript (if any):
# Estimated time spent (hr):6
# Description of any added extensions:
########################################
from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random


def wordle():
    # The main function to play the Wordle game.
    gw = WordleGWindow() 
    
    def enter_action():
        guess = ""
        
        for i in range(5):
            guess += gw.get_square_letter(gw.get_current_row(),i)
        print(guess)
        guess = guess.lower()
        #check if the word typed is english
        if is_english_word(guess):
            gw.show_message("word is english")
        else:
            gw.show_message("not valid word")
        #set the color of the letters if letters are correct
        for i in range(5):
            letter = gw.get_square_letter(gw.get_current_row(),i).lower()
            if answer[i]==guess[i]:
                gw.set_square_color(gw.get_current_row(),i,CORRECT_COLOR)

            elif answer[i]!=guess[i] and guess[i] in answer:
                gw.set_square_color(gw.get_current_row(),i,PRESENT_COLOR)

            else:
                gw.set_square_color(gw.get_current_row(),i,MISSING_COLOR)
        #move rows?
        while guess != answer:
            gw.get_current_row == gw.set_current_row(+1)
            
        #finish the game
        if guess == answer:
            gw.show_message("YOU GOT IT!")
            gw.set_current_row(N_ROWS) 

        #create a random 5 letter word as the answer 
    def random_word():
        answer = random.choice(ENGLISH_WORDS).lower()
        while len(answer)!= 5:
            answer = random.choice(ENGLISH_WORDS).lower()
        print(answer.lower())
        return(answer.lower())
 
    answer = random_word()    
    
    
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

        
    # to see if a word is in ENGLISH_WORDS, make it lower case.
    guess_str = "Hello"
    guess_low = guess_str.lower()
    guess_cap = guess_str.upper()
    print(guess_str, guess_str in ENGLISH_WORDS) # Hello False
    print(guess_low, guess_low in ENGLISH_WORDS) # hello True
    print(guess_cap, guess_cap in ENGLISH_WORDS) # HELLO False

    # places 'H' in the upper left
    #gw.set_square_letter(0,0,guess_cap[0])
    #gw.get_square()


# Startup boilerplate
if __name__ == "__main__":
