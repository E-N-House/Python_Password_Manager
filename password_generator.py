# Password Generator Project
from random import choice, randint, shuffle
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    """generates a random amount of letters caps and lower case english alphabet, numbers and symbols
    then shuffles the lists to return a string of random characters"""

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    random_letters = [choice(LETTERS) for _ in range(nr_letters)]
    random_numbers = [choice(NUMBERS) for _ in range(nr_numbers)]
    random_symbols = [choice(SYMBOLS) for _ in range(nr_symbols)]
    password_list = random_symbols + random_numbers + random_letters

    shuffle(password_list)
    password = "".join(password_list)
    return password
