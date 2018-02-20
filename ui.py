import accounts


def print_program_menu(menu_commands):
    for option in menu_commands:
        print('(' + str(menu_commands.index(option)) + ')' + '  ----->  ' + option)


def menu():
    option = ''
    while option != '8':
        print ('Main menu:')
        menu_commands = ['Creat an account', 'Log in', 'Generate Picture', 'Save your changes & Quit']
        print_program_menu(menu_commands)
        option = input('Choose an option: ')
        if option == '0':
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_)
        elif option == '1':
            print('gen')
        elif option == '1':
            print('gen')
        elif option == '8':
            break
        else:
            display.print_command_result('TREHE IS NO SUCH OPTION')

