'''
This module includes functions that convert from one element to another
'''

def encode(solution):
    '''
    Takes the input of player 1 and converts it into dashes.
    '''
    solution = str(solution)
    encode_solution = ""
    for char in solution:
        if char.isalpha():
            encode_solution += '*'
        else:
            encode_solution += char
    return encode_solution

def decode(solution, answer, display):
    '''
    Converts  the dashes into the correctly guessed letter
    '''
    
    for i, char in enumerate(solution):
        if char == answer:
            display = display[:i] + char + display[i+1:]
        else:
            pass

    return display

def hint_conversion(hint):
    if hint == "a":
        return "an animal"

    if hint == "f":
        return "a fruit"

    if hint == "c":
        return "a country"
    
    raise ValueError()