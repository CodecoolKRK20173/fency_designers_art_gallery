import sys
import pictures
import data_manager
import accounts


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
                return login
            else:
                print('Wrong password!')
        else:
            print('Wrong login, check spelling or create new account!')
            log = 0


def profile_menu(login):
    option = ''
    menu_commands = ['Show my gallery', 'Generate new art', 'Save your changes & Quit to main menu']
    while option != '3':
        print_menu(menu_commands)
        option = input('Choose an option: ')
        if option == "1":
<<<<<<< HEAD
            picture = accounts.load_accounts_and_pass('login')
            pictures.display_picture(picture)
=======
            picture = data_manager.import_from_file(login)
            pictures.display_picture(picture)

>>>>>>> 0341053b654298aa408a05c7f70bff95b86b27a9
        elif option == "2":
            picture = pictures.generate_picture()
            pictures.display_picture(picture)
            choose_picture(login, picture)
 

def menu():
    option = ''
    menu_commands = ['Create an account', 'Log in', "Show public gallery", "Show best arts", 'Quit']
    while True:
        print ('Main menu:')
        print_menu(menu_commands)
        option = input('Choose an option: ')
        if option == '1':
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_)
        elif option == '2':
            profile_menu(log_in())
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
<<<<<<< HEAD
        pictures.change_picture(picture)
=======
        picture = pictures.change_picture(picture)
        pictures.display_picture(picture)
        choose_picture(login, picture)   
>>>>>>> 0341053b654298aa408a05c7f70bff95b86b27a9

    elif decision == "2":
        percent_of_change = 0.6
        picture = pictures.change_picture(picture, percent_of_change)
        pictures.display_picture(picture)
        choose_picture(login, picture)

    elif decision == "3":
<<<<<<< HEAD
        gallery_ = pictures.gallery(picture, 'login')
        accounts.saving_accounts_and_pass(gallery_, 'login')
        "Your picture is saved in gallery"
=======
        data_manager.export_to_file(login, picture)
        print("Your picture is saved in gallery")
>>>>>>> 0341053b654298aa408a05c7f70bff95b86b27a9

