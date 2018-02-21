import accounts
import sys
import pictures
import data_manager

def print_menu(menu_commands):
    for option in menu_commands:
        print('(' + str(menu_commands.index(option) + 1) + ')' + '  ----->  ' + option)


def log_in():
    accounts_ = accounts.load_accounts_and_pass()
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


def profile(login):
    option = ''
    menu_commands = ['Show my gallery', 'Generate new art', 'Save your changes & Quit to main menu']
    while option != '3':
        print_program_menu(menu_commands)
        option = input('Choose an option: ')
        if option == "0":
            data_manager.import_from_file(login)
        elif option == "1":
            picture = pictures.generate_picture()
            choose_picture(login, picture)

        

def menu():
    option = ''
    menu_commands = ['Create an account', 'Log in', 'Save your changes & Quit']
    while option != '0':
        print ('Main menu:')
        print_menu(menu_commands)
        option = input('Choose an option: ')
        if option == '1':
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_)
        elif option == '2':
            profile(log_in())
        elif option == '3':
            print('gen')
        elif option == '0':
            print('bye!')
            sys.exit()
        else:
            display.print_command_result('TREHE IS NO SUCH OPTION')

def choose_picture(login, picture):
    decision = input("How do you like this picture?\n")
    options = ["Pretty", "Ugly", "Masterpiece - save!"]
    print_menu(options)

    if decision == "0":
        percent_of_change = "motzno"

    elif decision == "1":
        percent_of_change = "troszku"

    elif decision == "2":
        data_manager.export_picture(login, picture)







