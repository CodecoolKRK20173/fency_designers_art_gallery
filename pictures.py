import random


def get_random_proportion():

    RED = "\033[1;31;40m"
    NORMAL = "\033[0m"
    WHITE = "\033[1;37m"
    DARK_GREY = "\033[1;30;40m"
    BRIGHT_CYAN = "\033[1;36;40m"
    GREEN = "\033[1;32;40m"
    DARK_GREEN = ""
    GOLD = "\033[1;33;40m"
    BRIGHT_BLUE = "\033[0;34;40m"

    colors_list = [RED, WHITE, NORMAL, BRIGHT_BLUE, BRIGHT_CYAN, GREEN, GOLD]

    colors_dict = {}

    for color in colors_list:
        value = random.randint(1,5)
        if color not in colors_dict:
            colors_dict[color] = value

    proportion_list = []

    for key, value in colors_dict.items():
        proportion = [key] * value
        proportion_list.extend(proportion)

    # print(colors_dict)
    # print(proportion_list)

    return proportion_list



def generate_picture(color_list):

    sign = "▒"

    number_of_columns = int(input("Please enter width of picture: ")) * 2
    number_of_rows = int(input("Please enter heigh of picture: "))


    characters_number = number_of_columns * number_of_rows 
    characters_list = []
    """    characters_list = number_of_columns * number_of_rows * [sign]
    print(characters_list)"""

    for index in range(characters_number):
        characters_list.append(random.choice(color_list) + sign)
        

    NORMAL = "\033[0m"


    k = number_of_columns - 1
    j = 0
    for i in range(number_of_rows):
        print("".join(characters_list[j:k]) + NORMAL)
        j = k
        k += number_of_columns - 1
       

def main():
    color_list = get_random_proportion()
    generate_picture(color_list)


if __name__ == "__main__":
    main()