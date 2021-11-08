'''
This module is where the functions will be implemented in cohesive lines of code
'''
import os
import art
from colorama import Fore, Style
from hangman_functions import encode, decode, answer_test, hangman_draw, guess_store, guess_test, rand_word, hint_conversion

def main():
    game_style = input("Single or Multiplayer (s/m)?\n")

    if game_style == "m":
        print("----------------")
        print("PLAYER ONE TURN")
        print("----------------")

        hint = input("What is your hint?\n")
        solution = input("What is the answer?\n")
        solution = solution.upper()

        os.system('clear')
    elif game_style == "s":
        hint = input("Do you want to guess fruits, countries or animals(a/c/f)?\n")
        solution = rand_word(hint)
        solution = solution.upper()
        hint = hint_conversion(hint)

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
            
            print(Fore.RED + "WRONG GUESS")
            print(hangman_draw(count) + Style.RESET_ALL + "\n")
            print(Fore.MAGENTA + "HINT: " + hint + "\n" + Style.RESET_ALL)
            print(display + "\n")
            
        elif answer_test(answer, solution) == True:
            os.system('clear')
            if guess_test(answer, past_guess) == True:
                pass
            
            display = decode(solution, answer, display)
            
            print(Fore.MAGENTA + "HINT: " + hint + "\n" + Style.RESET_ALL)
            print(hangman_draw(count) + "\n")
            print(display + "\n")
        
        if count == 6:
            os.system('clear')
            
            print(Fore.RED + display)
            print(Fore.GREEN + "THE SOLUTION IS: {}\n".format(solution) + Style.RESET_ALL)

            print(Fore.RED + "Sorry, you're not very good at this game.\nAnd, you've been hung!!")
            
            art.tprint("YOU LOSE!!")
            

        if display == solution:
            
            os.system('clear')
            print(Fore.GREEN)
            print(hangman_draw(count) + "\n")
            print(display)
            art.tprint("YOU WIN!!")
            status = 'n'

        past_guess = guess_store(answer, past_guess)
        
if __name__ == "__main__":
    main()