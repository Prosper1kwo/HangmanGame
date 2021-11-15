'''
These functions test some values in the game,
returning True or False
'''

from hangman_pics import hang_image


def hangman_draw(error_count):
    '''
  Returns an ASCII image of a hanged-man based on the player's error_count
  '''

    if error_count == 0:
        return hang_image[0]
    if error_count == 1:
        return hang_image[1]
    if error_count == 2:
        return hang_image[2]
    if error_count == 3:
        return hang_image[3]
    if error_count == 4:
        return hang_image[4]
    if error_count == 5:
        return hang_image[5]
    if error_count == 6:
        return hang_image[6]
        # print('YOU LOSE!!')
    raise ValueError()
    
def answer_test(answer, solution):
    '''
    Checks if the letter guessed by player 2 is in the solution variable.
    '''
    if answer.upper() in solution.upper():
        return True
    else:
        return False

def guess_test(answer, past_guess):
    '''
    Checks if the letter guessed is in the list of
    guessed answers and return true or false.
    '''
    if answer in past_guess:
        print("You have already guessed this letter, here is a list of your guesses: {}\n".format(past_guess) )
        return True
    else:
        return False