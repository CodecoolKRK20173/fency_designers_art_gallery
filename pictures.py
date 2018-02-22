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



def generate_picture():
    color_list = get_random_proportion()

    signs = get_random_sign_list()

    number_of_columns = int(input("Please enter width of picture: "))
    number_of_rows = int(input("Please enter heigh of picture: "))
    picture_name = input("Enter picture name: ")
    characters_list = []

    element = [""] * number_of_columns

    for i in range(number_of_rows):
        characters_list.append(element[:])

    for line in characters_list:
        for element in range(len(line)):
            line[element] = random.choice(color_list) + random.choice(signs)
    picture_dict = {}
    picture_dict[picture_name] = characters_list
    return picture_dict


def get_random_sign_list():
    signs = ["██", "▐░", "▒▒", "░░", "░▒", "▒░", "▓▓"]
    x = random.randint(0, len(signs))
    sign_list = []

    for i in range(0, x):
        sign_list.append(random.choice(signs))

    return sign_list


def display_picture(gallery):
    
    NORMAL = "\033[0m"

    # for line in characters_list:
    #     print("".join(line) + NORMAL)

    # for key, value in gallery.items():
    #     print(key)
    #     print("".join(value) + NORMAL)

    
    for key, value in gallery.items():
        print(key)
        for line in value:
            print("".join(line)+ NORMAL)


def change_picture(characters_list, percent_of_change = 0.2):
    color_list = get_random_proportion()
    x = len(characters_list)
    for index in range(int(x*0.2)):
        for line in characters_list:
            for element in range(len(line)):
                line[element] = random.choice(color_list) + random.choice(signs)
        
    return characters_list
       

def main():
    color_list = get_random_proportion()
    picture_dict = generate_picture(color_list)
    # gallery = gallery(characters_list)
    display_picture(picture_dict)


if __name__ == "__main__":
    main()