
'''
This module is where the functions will be implemented in cohesive lines of code
'''
import os
import art
from colorama import Fore, Style
from conversion_functions import decode, encode, hint_conversion 
from store_functions import rand_word, guess_store
from test_functions import hangman_draw, answer_test, guess_test
from replit import audio

def main():
    audio.play_file('title_audio.wav')
    
    art.tprint("HANGMAN" , font="block" , chr_ignore=True) 
    
    game_style = input("Single or Multiplayer (s/m)?\n")

    while game_style.lower() not in "sm":
        game_style = input("Single or Multiplayer (s/m)?\n")

    if game_style.lower() == "m":
        print("----------------")
        print("PLAYER ONE TURN")
        print("----------------")

        hint = input("What is your hint?\n")
        solution = input("What is the answer?\n")
        solution = solution.upper()

        os.system('clear')

        print("----------------")
        print("PLAYER TWO TURN")
        print("----------------")


    elif game_style.lower() == "s":
        hint = input("Do you want to guess fruits, countries or animals(a/c/f)?\n")
        while hint.lower() not in "acf":
            hint = input("Do you want to guess fruits, countries or animals(a/c/f)?\n")
        
        solution = rand_word(hint.lower())
        solution = solution.upper()
        hint = hint_conversion(hint.lower())
        
        os.system('clear')

        print("----------------")
        print("TIME TO GUESS!!!")
        print("----------------")
    

    print("Your hint is: {}".format(hint))
    past_guess = []
    display = encode(solution)
    print(display)

    status = input("Are you ready? y/n?\n")

    while status.lower() != 'y':
        status = input("Are you ready? y/n?\n")
        
    count = 0
    print(hangman_draw(count) + "\n")
    print(display + "\n")

    while status.lower() == "y" and count != 6:
        answer = input("What is your guess?\nYou have guessed the following letters: {}\n".format(past_guess))
        answer = answer.upper()
        
        if answer_test(answer, solution) == False:
            os.system('clear')

            guess_test(answer, past_guess)
            count += 1

            if count < 6:
                audio.play_file('whistle_error.wav')
            
            print(Fore.RED + "WRONG GUESS")
            print(hangman_draw(count) + Style.RESET_ALL + "\n")
            print(Fore.MAGENTA + "HINT: " + hint + "\n" + Style.RESET_ALL)
            print(display + "\n")
            
        elif answer_test(answer, solution) == True:
            os.system('clear')

            if display != solution:
                audio.play_file('correct_answer.wav')

            if guess_test(answer, past_guess) == True:
                pass
            
            display = decode(solution, answer, display)
            
            print(Fore.MAGENTA + "HINT: " + hint + "\n" + Style.RESET_ALL)
            print(hangman_draw(count) + "\n")
            print(display + "\n")
        
        if count == 6:
            os.system('clear')

            audio.play_file('game_over.wav')

            print(Fore.RED + display)
            print(Fore.GREEN + "THE SOLUTION IS: {}\n".format(solution) + Style.RESET_ALL)

            print(Fore.RED + "Sorry P2, you're not very good at this game.\nAnd, you've been hung!!")
            print(hangman_draw(count))
            
            if game_style.lower() == "m":
                art.tprint("PLAYER  ONE  WINS!!")
            else:
                art.tprint('YOU  LOSE!!')
            

        if display == solution:
            os.system('clear')

            audio.play_file('game_complete.wav')

            print(Fore.GREEN + hangman_draw(count) + "\n")
            print(display)

            if game_style.lower() == "m":
                art.tprint("PLAYER  TWO  WINS!!")
            else:
                art.tprint('YOU  WIN!!')
            status = 'n'

        past_guess = guess_store(answer, past_guess)
        
if __name__ == "__main__":
    main()