import random

#definicje
def ask_number(nb_min, nb_max):
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the magic number (between {nb_min} and {nb_max})? :")
        try:
            number_int = int(number_str)
        except:
            print("EROOR: Magic number must be a number. Please, try again.")
        else:
            if number_int < nb_min or number_int > nb_max:
                print(f"ERROR: You must enter the number between {nb_min} and {nb_max}! Please, try again.")
                number_int = 0
    return number_int

#dane
MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4

#kod
number = 0
lives = NB_LIVES
while number != MAGIC_NUMBER and lives > 0:
    print(f"You have {lives} lives left!")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number < MAGIC_NUMBER:
        print("Magic number is greater")
        lives -= 1
    elif number > MAGIC_NUMBER:
        print("Magic number is lower")
        lives -= 1
    elif number == MAGIC_NUMBER:
        print("You won!")

if lives == 0:
    print(f"You lost! The magic number wa {MAGIC_NUMBER}!")