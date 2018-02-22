import sys
import pictures
import data_manager
import accounts
import os
from magic_menu import *



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
            if os.path.isfile(login + '.json'):
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
            input("Press Enter to continue...")
        if index_ == 2 and choice == 1:
            rating_pictures()
        if index_ == 3 and choice == 1:
            logged_in = False


def menu():
    menu_commands = ['Create an account', 'Log in', "Show public gallery", "Show best arts", 'Quit']
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
            print("Log in to give a grade to picture or create your own")
            rating_pictures()
        if index_ == 3 and choice == 1:
            print("The best of :)")
        if index_ == 4 and choice == 1:
            program = False


def choose_picture(login, picture):
    edit = True
    while edit:
        options = ["Pretty but change it a little bit", "Ugly - show me something else!", "Masterpiece - save!"]
        print_menu(options)
        print("How do you like this picture?\n")
        decision = getch()

        if decision == "1":

            picture = pictures.change_picture(picture)
            pictures.display_picture(picture)

        elif decision == "2":
            percent_of_change = 0.6
            picture = pictures.change_picture(picture, percent_of_change)
            pictures.display_picture(picture)

        elif decision == "3":
            gallery_ = pictures.make_gallery(picture, login)
            data_manager.export_to_file(login, gallery_)
            edit = False
            print("Your picture is saved in gallery")


def rating_pictures():
    artists = []
    accounts_ = accounts.load_accounts_and_pass('accounts')

    for key, value in accounts_.items():
        artists.append(key)

    for artist in artists:
        print(artist)
    choice = input('Choose artist to display his/her work: ')

    if choice in artists:
        if os.path.isfile(choice + '.json'):
            picture = data_manager.import_from_file(choice)
            pictures.display_gallery(picture)
        else:
            print('Artist has no paintings')
    else:
        print('No such artist!')
