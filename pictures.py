import random
import sys


def generate_picture():

    RED = "\033[1;31;40m"
    NORMAL = "\033[0m"
    WHITE = "\033[1;37m"
    DARK_GREY = "\033[1;30;40m"
    BRIGHT_CYAN = "\033[1;36;40m"
    GREEN = "\033[1;32;40m"
    DARK_GREEN = ""
    GOLD = "\033[1;33;40m"
    BRIGHT_BLUE = "\033[0;34;40m"


    color_list = [RED, WHITE, BRIGHT_CYAN, BRIGHT_BLUE, GOLD, GREEN]

    sign = "▒"

    number_of_columns = int(input("Please enter width of picture: ")) * 2
    number_of_rows = int(input("Please enter heigh of picture: "))


    characters_number = number_of_columns * number_of_rows 
    characters_list = []
    """    characters_list = number_of_columns * number_of_rows * [sign]
    print(characters_list)"""

    for i in range(characters_number):
        characters_list.append(random.choice(color_list)+sign)

    

    k = number_of_columns - 1
    j = 0
    for i in range(number_of_rows):
        print("".join(characters_list[j:k]) + NORMAL)
        j = k
        
        k += number_of_columns - 1

    return characters_list
       



generate_picture()