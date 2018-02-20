import sys
import accounts


def print_menu(menu_commands):
    for option in menu_commands:
        print('(' + str(menu_commands.index(option)) + ')' + '  ----->  ' + option)


def menu():
    option = ''
    while option != '8':
        print ('Main menu:')
        menu_commands = ['Creat an account', 'Log in', 'Generate Picture', 'Save your changes & Quit']
        print_menu(menu_commands)
        option = input('Choose an option: ')
        if option == '0':
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_)
        elif option == '1':
            print('gen')
        elif option == '1':
            print('gen')
        elif option == '8':
            sys.exit()
        else:
            display.print_command_result('TREHE IS NO SUCH OPTION')

def choose_picture(picture):
    decision = input("How do you like this picture?\n")
    options = ["Pretty", "Ugly", "Masterpiece - save!"]
    print_menu(options)

    if decision == "0":
        percent_of_change = "motzno"

    elif decision == "1":
        percent_of_change = "troszku"

    elif decision == "2":
        data_manager.export_picture(picture)






