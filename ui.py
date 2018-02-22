import sys
import pictures
import data_manager
import accounts
import os


def print_menu(menu_commands):
    for option in menu_commands:
        print('(' + str(menu_commands.index(option) + 1) + ')' + '  ----->  ' + option)


def log_in():
    accounts_ = accounts.load_accounts_and_pass('accounts')
    log = 1
    login = input('Login: ')

    while log != 0:
        if login in accounts_:
            password = input('Password: ')
            if password == accounts_[login]:
                print('profile')
                log = 0
                profile_menu(login)
                return login
            else:
                print('Wrong password!')
        else:
            print('Wrong login, check spelling or create new account!')
            log = 0


def profile_menu(login):
    print(login)
    option = ''
    menu_commands = ['Show my gallery', 'Generate new art', 'Rate paintings', 'Save your changes & Quit to main menu']
    while option != '4':
        print_menu(menu_commands)
        option = input('Choose an option: ')
        if option == "1":
            if os.path.isfile(login + '.json'):
                picture = data_manager.import_from_file(login)
                pictures.display_gallery(picture)
            else:
                print('Your gallery is empty')
        elif option == "2":
            picture = pictures.generate_picture()
            pictures.display_picture(picture)
            choose_picture(login, picture)
        elif option == '3':
            display_artists()


def menu():
    option = ''
    menu_commands = ['Create an account', 'Log in', "Show public gallery", "Show best arts", 'Quit']
    while True:
        print ('Main menu:')
        print_menu(menu_commands)
        option = input('Choose an option: ')
        if option == '1':
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_, 'accounts')
        elif option == '2':
            log_in()
        elif option == '3':
            print("Log in to give a grade to picture or create your own")
            profile_menu("Beniz")
            """Function showing all pictures of all artist and it's prices"""
        elif option == '4':
            print("The best of :)")
        elif option == '5':
            print('bye!')
            sys.exit()
        else:
            display.print_command_result('THERE IS NO SUCH OPTION')


def choose_picture(login, picture):

    options = ["Pretty but change it a little bit", "Ugly - show me something else!", "Masterpiece - save!"]
    print_menu(options)
    decision = input("How do you like this picture?\n")

    if decision == "1":

        picture = pictures.change_picture(picture)
        pictures.display_picture(picture)
        choose_picture(login, picture)   


    elif decision == "2":
        percent_of_change = 0.6
        picture = pictures.change_picture(picture, percent_of_change)
        pictures.display_picture(picture)
        choose_picture(login, picture)

    elif decision == "3":
        gallery_ = pictures.make_gallery(picture, login)
        data_manager.export_to_file(login, gallery_)
        print("Your picture is saved in gallery")

def display_artists():
    artists = []
    accounts_ = accounts.load_accounts_and_pass('accounts')
    for key, value in accounts_.items():
        artists.append(key)
    for artist in artists:
        print(artist)
    choice = input('Choose artist to display his/her work: ')

    if choice in artists:
        picture = data_manager.import_from_file(choice)
        pictures.display_gallery(picture)
    else:
        print('No such artist!')