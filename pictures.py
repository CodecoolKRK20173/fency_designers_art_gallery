import random
import accounts
import os.path
import data_manager
import os

def get_colors_data():

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

    return colors_list



def get_random_proportion():

    colors_list = get_colors_data()

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



def make_gallery(picture, login, grade =['5']):
    name = input("Enter picture name: ")
    file_ = login + '.json'
    if os.path.isfile(file_):
        gallery = data_manager.import_from_file(login)
    else:
        gallery = {}
    gallery[name] = {"picture" : picture, "ocena" : grade}
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

    for picture in dictionary:
        print("\nName of picture: " + picture)
        for picture_data in dictionary[picture]:          
            for paint in dictionary[picture][picture_data]:
                if len(paint) > 1:
                    print("".join(paint) + NORMAL)
                else:
                    print("\nPicture graded as: " + "".join(paint) + "\n")



def display_picture(picture):

    NORMAL = "\033[0m"
    os.system('clear')
    for line in picture:
        print("".join(line) + NORMAL)


def change_picture(picture, percent_of_change = 0.1, harmony = 0):
    color_list = get_colors_list(percent_of_change)
    range_ = len(picture)
    signs = get_random_sign_list()


    x = int(len(picture)*percent_of_change)
    if x < 1:
        x = 1

    for index in range(x):
        for line in picture:

                if harmony == 0:
                    make_more_chaos(line, color_list, signs, range_)
                else:
                    make_more_harmony(line, color_list, signs, range_)


    return picture

def make_more_chaos(line, color_list, signs, range_):
    sectors = get_random_sectors()
    i = int(len(color_list)/2)

    change_level = random.randint(0,1)
    for index, element in enumerate(line):

        if change_level == 1: 
            if index < int(range_/sectors):
                line[index] = random.choice(color_list[0:i]) + random.choice(signs)
            else:
                line[index] = random.choice(color_list[i:-1]) + random.choice(signs)
        
        else:
            if index > int(range_/sectors):
                line[index] = random.choice(color_list[0:i]) + random.choice(signs)
            else:
                line[index] = random.choice(color_list[i:-1]) + random.choice(signs)



def make_more_harmony(line, color_list, signs, range_):
    i = int(len(color_list)/2)

    for index, element in enumerate(line):

        if index < int(range_/2):
            line[index] = random.choice(color_list[0:i]) + random.choice(signs)
        else:
            line[index] = random.choice(color_list[i:-1]) + random.choice(signs)

#def shake_it_up()

    

def get_random_sectors():
    number_of_sectors = random.randint(1, 3)
    return number_of_sectors


def change_colors(option, color, colors_list_for_user):
    color_proportions = data_manager.import_from_file("proportions")
    color_list = get_colors_data()
    color_to_change = color_list[color]

    if option == 1:
        color_proportions = list(filter(lambda a: a != color_to_change, color_proportions))
        colors_list_for_user.remove(colors_list_for_user[color])


    elif option == 2: 
        color_proportions.append(color_to_change)

    elif option == 3:
        X = len(color_list)
        Y = len(color_proportions)
        index = random.randint(X, Y)
        for i in range(index):
            color_proportions.insert(Y, color_to_change)

    elif option == 4:
        for color_to_change in color_proportions:
            index = random.randint(0, 1)
            if index == 1:
                color_proportions.remove(color_to_change)


    data_manager.export_to_file("proportions", color_proportions, "w")

    return colors_list_for_user

def choose_sector(picture, sector):
    x = len(picture)//3
    y = len(picture[0])//3
    w = len(picture) % 3
    z = len(picture[0]) % 3
    if sector < 10:
        if sector == 1 or sector == 4 or sector == 7:
            a = 0
            b = 1 * y
        elif sector == 2 or sector == 5 or sector == 8:
            a = y
            b = 2 * y
        elif sector == 3 or sector == 6 or sector == 9:
            a = 2 * y 
            b = 3 * y+z
        if sector < 4:
            c = 0
            d = 1 * x
        elif sector > 3 and sector < 7:
            c = x
            d = 2 * x
        elif sector > 6:
            c = 2 * x 
            d = 3 * x + w

    chosen_sector = [line[a:b] for line in picture[c:d]]
    data_list = [a, b, c, d]

    return chosen_sector, data_list
    


def replace_changed_sector(picture, chosen_sector, data_list):
    a = data_list[0]
    b = data_list[1]
    c = data_list[2]
    d = data_list[3]
    k = 0

    for old_line in picture[c:d]:
        j = 0
        for i in range(a, b):
            old_line[i] = chosen_sector[k][j]
            j += 1

        k += 1
            


    return picture

#def append_chosen_sector(picture, chosen_sector, sector):










def get_colors_list(percent_of_change):
    colors_list = data_manager.import_from_file("proportions")
    colors_list = random.sample(colors_list, len(colors_list))
    x = int(percent_of_change*len(colors_list))
    if x < 1:
        x = 1

    for i in range(x):
        j = random.randint(0, len(colors_list)-1)
        if colors_list[i] != colors_list[j]:
            colors_list[i] = colors_list[j]
        
    return colors_list
