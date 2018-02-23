import sys
import pictures
import data_manager
import accounts
import os
from magic_menu import *
import json
import operator



def print_menu(menu_commands):
    for option in menu_commands:
        print('(' + str(menu_commands.index(option) + 1) + ')' + '  ----->  ' + option)


def log_in():
    accounts_ = accounts.load_accounts_and_pass('accounts')
    logged_in = False

    while not logged_in:
        login = input('Login: ')
        if login in accounts_:
            password = input('Password: ')
            if password == accounts_[login]:
                print('profile')
                logged_in = True
                profile_menu(login)
                return login
            else:
                print('Wrong password!')
        else:
            print('Wrong login, check spelling or create new account!')
            logged_in = False


def profile_menu(login):
    print('logged as: ' + login)
    menu_commands = ['Show my gallery', 'Generate new art', 'Rate paintings', 'Save your changes & logout']
    index_ = 0
    i = 0
    logged_in = True
    while logged_in:
        print_magic_menu(menu_commands, index_, 'logged as: ' + login)
        index_, choice = get_input(index_, menu_commands)
        if index_ == 0 and choice == 1:
            if os.path.isfile("profiles/" + login + '.json'):
                picture = data_manager.import_from_file(login)
                pictures.display_gallery(picture)
                input("Press Enter to continue...")
            else:
                print('Your gallery is empty')
                input("Press Enter to continue...")

        if index_ == 1 and choice == 1:
            picture = pictures.generate_picture()
            pictures.display_picture(picture)
            choose_picture(login, picture)
        if index_ == 2 and choice == 1:
            picture = rating_pictures()
            gallery_ = grade_picture(picture)
            data_manager.export_to_file(login, gallery_)
        if index_ == 3 and choice == 1:
            logged_in = False


def menu():
    menu_commands = ['Create an account', 
                    'Log in', "Show public gallery", 
                    "Show gallery of given artist", 
                    "Show best arts", 'Quit']
    index_ = 0
    i = 0
    program = True

    while program:
        print_magic_menu(menu_commands, index_, 'Main menu:')
        index_, choice = get_input(index_, menu_commands)

        if index_ == 0 and choice == 1:
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_, 'accounts')
        if index_ == 1 and choice == 1:
            log_in()
        if index_ == 2 and choice == 1:
            all_paintings = get_all_files()
            all_dictionaries = get_all_paintings(all_paintings)
            sorted_dictionaries = get_sorted_dictionaries(all_dictionaries)
            pictures.display_gallery(all_dictionaries, sorted_dictionaries)
            input("Press Enter to continue...")

        if index_ == 3 and choice == 1:
            show_public_gallery()
        if index_ == 4 and choice == 1:
            all_paintings = get_all_files()
            all_dictionaries = get_all_paintings(all_paintings)
            sorted_dictionaries = get_sorted_dictionaries(all_dictionaries)
            best_pictures = get_best_pictures(sorted_dictionaries)
            pictures.display_gallery(all_dictionaries, best_pictures)
            input("Press Enter to continue...")

        if index_ == 5 and choice == 1:
            program = False



def choose_picture(login, picture):
    edit = True
    while edit:
        options = ["I want more harmony!", 
                    "Give me some chaos!", 
                    "I need something complately else", 
                    "Change coloristics", 
                    "Turn on sector changing mode",
                    "Turn off sector changing mode",
                    "Masterpiece - save!"]
        print_menu(options)
        print("How do you like this picture?\n")
        decision = getch()
        
        if decision == "1":

            picture = pictures.change_picture(picture, harmony = 1)
            pictures.display_picture(picture)

        elif decision == "2":
            percent_of_change = 0.6
            picture = pictures.change_picture(picture, percent_of_change)
            pictures.display_picture(picture)

        elif decision == "3":
            picture = pictures.generate_picture()
            pictures.display_picture(picture)
            

        elif decision == "4":
            percent_of_change = manipulate_color_menu()
            picture = pictures.change_picture(picture, percent_of_change)
            pictures.display_picture(picture)

        elif decision == "5":
            try:            
                sector = int(input(" 1  2  3\n 4  5  6\n 7  8  9\n Choose number of sector you want to change: "))
            except ValueError:
                print("You entered wrong data")
            temp = picture
            picture, data_list = pictures.choose_sector(temp, sector)
            pictures.display_picture(pictures.replace_changed_sector(temp, picture, data_list))

        elif decision == "6":
            try:
                picture = pictures.replace_changed_sector(temp, picture, data_list)
                print("Sector changing mode turned off")
                pictures.display_picture(picture)
            except UnboundLocalError:
                print("You are not in sector changing mode yet ;)")        

        elif decision == "7":
            gallery_ = pictures.make_gallery(picture, login)
            data_manager.export_to_file(login, gallery_)
            edit = False
            print("Your picture is saved in gallery")

        elif decision == "q":
            sys.exit()

        
        




def manipulate_color_menu():
    options = ["Delete one of colors in palette", 
                "Add one of colors in palette", 
                "I want more of one of colors!", 
                "I want less of one of colors"]

    print_menu(options)
    colors_list = ["RED", "SNOWY EVENING", "WHITE", "BRIGHT BLUE", "BRIGHT CYAN", "GREEN", "GOLD"]
    
    try:
        coloristics = int(input("Choose an option: "))
        print_menu(colors_list)
        color = int(input("Choose color number: ")) - 1
        colors_list = pictures.change_colors(coloristics, color, colors_list)
        if coloristics < 3:
            change = 1
        else:
            change = 0.5

        return change


    except ValueError:
        print("Wrong input")
        manipulate_color_menu()
    






def show_public_gallery():
    artists = []
    accounts_ = accounts.load_accounts_and_pass('accounts')

    for key, value in accounts_.items():
        artists.append(key)

    for artist in artists:
        print(artist)
    choice = input('Choose artist to display his/her work: ')

    if choice in artists:
        if os.path.isfile('profiles/' + choice + '.json'):
            picture = data_manager.import_from_file(choice)
            pictures.display_gallery(picture)
        else:
            print('Artist has no paintings')
    else:
        print('No such artist!')


def rating_pictures():
    artists = []
    accounts_ = accounts.load_accounts_and_pass('accounts')

    for key, value in accounts_.items():
        artists.append(key)

    for artist in artists:
        print(artist)
    choice = input('Choose artist to display his/her work: ')

    if choice in artists:
        if os.path.isfile('profiles/' + choice + '.json'):
            picture = data_manager.import_from_file(choice)
            return picture
        else:
            print('Artist has no paintings')
    else:
        print('No such artist!')


def grade_picture(dictionary):
    
    NORMAL = "\033[0m"

    for picture_name in dictionary:
        print("\nName of picture: {} \n".format(picture_name))
        for paint in dictionary[picture_name]["Picture"]:
            print("".join(paint) + NORMAL)
        
        print("Picture graded as: {} \n".format(dictionary[picture_name]["Grade"]))
        print("Picture price: {} $".format(dictionary[picture_name]["Price"]))
        print("Picture author: {}".format(dictionary[picture_name]["Author"]))

        grade = int(input("Rate this picture from 1 - 5: "))
        
        dictionary[picture_name]["Number of grades"] += 1
        number_of_grades = dictionary[picture_name]["Number of grades"]
        dictionary[picture_name]["Grade"] += (grade/number_of_grades)
        dictionary[picture_name]["Price"] += (grade * 50) * (number_of_grades/2)
        
    return dictionary


def get_all_files():
    all_json_files = os.listdir("profiles/")

    if "proportions.json" in all_json_files:
        all_json_files.remove("proportions.json")
    if "sector_data.json" in all_json_files:
        all_json_files.remove("sector_data.json")
    return all_json_files


def get_all_paintings(all_dictionaries):
    all_paintings = {}

    for filename in all_dictionaries:
        with open("profiles/" + filename) as imported_dictionaries:
            user_gallery = json.load(imported_dictionaries)
        for key in user_gallery:
            all_paintings[key] = user_gallery[key]
    return all_paintings


def get_sorted_dictionaries(all_dictionaries):
    sorted_paintings = sorted(all_dictionaries, key=lambda x: (all_dictionaries[x]["Grade"]))
    return sorted_paintings


def get_best_pictures(sorted_paintings):
    best_pictures = []


    for i in range(10):
        try:
            best_pictures.append(sorted_paintings[i])
        except IndexError:
            return best_pictures

    return best_pictures


        
        