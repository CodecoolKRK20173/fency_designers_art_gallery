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


    return proportion_list



def generate_picture(color_list):

    sign = "██"

    number_of_columns = int(input("Please enter width of picture: "))
    number_of_rows = int(input("Please enter heigh of picture: "))


    colors = random.choice(color_list) + sign

    characters_list = []

    element = [""] * number_of_columns

    for i in range(number_of_rows):
        characters_list.append(element[:])

    for line in characters_list:
        for element in range(len(line)):
            colors = random.choice(color_list) + sign
            line[element] = colors

    return characters_list


def display_picture(characters_list):
    
    NORMAL = "\033[0m"

    for line in characters_list:
        print("".join(line) + NORMAL)


def change_picture(characters_list, percent_of_change = 0.2):
    x = len(characters_list)
    for index in range(int(x*0.2)):
        
        element = random.randint(0, x)

        characters_list[element] = random.choice(characters_list)
        
    return characters_list
       

def main():
    color_list = get_random_proportion()
    characters_list = generate_picture(color_list)
    display_picture(characters_list)


if __name__ == "__main__":
    main()