import random
import string

def password_generator(min_length, number=True, special_character=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters

    if number:
        character += digits
    if special_character:
        character += special

    password = ""
    meet_criteria = False
    has_number = False
    has_special = False


    while not meet_criteria or len(password) < min_length:
        new_char = random.choice(character)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if number: 
            meet_criteria = has_number 
        if special_character:
            meet_criteria = meet_criteria and has_special



    return password
