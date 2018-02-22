import random
import accounts
import os.path
import data_manager



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

    data_manager.export_to_file("proportions", proportion_list, "w")


    return proportion_list



def generate_picture():
    color_list = get_random_proportion()
    signs = get_random_sign_list()
    is_numbers = False
    while is_numbers == False:
        number_of_columns = input("Please enter width of picture: ")
        number_of_rows = input("Please enter heigh of picture: ")
        try:
            if int(number_of_columns) > 0 and int(number_of_rows) > 0:
                is_numbers = True
        except ValueError:
            print("Wrong data provided!")

    characters_list = []

    element = [""] * int(number_of_columns)

    for i in range(int(number_of_rows)):
        characters_list.append(element[:])

    for line in characters_list:
        for element in range(len(line)):
            line[element] = random.choice(color_list) + random.choice(signs)

    return characters_list


def make_gallery(picture, login, grade =["5"]):
    name = input("Enter picture name: ")
    file_ = "profiles/" + login + '.json'
    if os.path.isfile(file_):
        gallery = data_manager.import_from_file(login)
    else:
        gallery = {}
    gallery[name] = {"Picture" : picture, "Grade" : grade}
    return gallery


def get_random_sign_list():
    signs = ["██", "▐░", "▒▒", "░░", "░▒", "▒░", "▓▓"]
    x = random.randint(1, len(signs))
    sign_list = []

    for i in range(0, x):
        sign_list.append(random.choice(signs))

    return sign_list


def display_gallery(dictionary):

    NORMAL = "\033[0m"

    # for picture in dictionary:
    #     print("\nName of picture: {} \n".format(picture))
    #     for picture_data in dictionary[picture]:          
    #         for paint in dictionary[picture][picture_data]:
    #             if len(paint) > 1:
    #                 print("".join(paint) + NORMAL)
    #             else:
    #                 print("Picture graded as: {} \n".format(paint))

    print(dictionary)
    for picture in dictionary:
        for picture_data in dictionary[picture]:
            for paint in range(len())
            




def display_picture(picture):

    NORMAL = "\033[0m"

    for line in picture:
        print("".join(line) + NORMAL)


def change_picture(picture, percent_of_change = 0.1):
    color_list = get_colors_list(percent_of_change)
    signs = get_random_sign_list()

    x = int(len(picture)*percent_of_change)
    if x < 1:
        x = 1

    for index in range(x):
        for line in picture:
            for index, element in enumerate(line):
                sectors = get_random_sectors()
                i = int(len(color_list)/sectors)
                #for i in range(sectors)

                if index < int(len(picture)/2):
                    line[index] = random.choice(color_list[0:i]) + random.choice(signs)
                else:
                    line[index] = random.choice(color_list[i:-1]) + random.choice(signs)

    return picture


def get_random_sectors():
    number_of_sectors = random.randint(1, 9)
    return number_of_sectors


def get_colors_list(percent_of_change):
    colors_list = data_manager.import_from_file("proportions")
    x = int(percent_of_change*len(colors_list))

    for i in range(x):
        j = random.randint(0, len(colors_list)-1)
        if colors_list[i] != colors_list[j]:
            colors_list[i] = colors_list[j]
        
    return colors_list
