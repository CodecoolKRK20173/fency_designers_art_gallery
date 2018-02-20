
import accounts


def print_program_menu(menu_commands):
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
                profile()
            else:
                print('Wrong password!')
        else:
            print('Wrong login, check spelling or create new account!')
            log = 0


def profile():
    option = ''
    menu_commands = ['Show my gallery', 'Generate new art', 'Save your changes & Quit to main menu']
    while option != '3':
        print_program_menu(menu_commands)
        option = input('Choose an option: ')
        


def menu():
    option = ''
    menu_commands = ['Creat an account', 'Log in', 'Save your changes & Quit']
    while option != '0':
        print ('Main menu:')
        print_program_menu(menu_commands)
        option = input('Choose an option: ')
        if option == '1':
            accounts_ = accounts.create_acc()
            accounts.saving_accounts_and_pass(accounts_)
        elif option == '2':
            log_in()
        elif option == '3':
            print('gen')
        elif option == '0':
            print('bye!')
        else:
            display.print_command_result('TREHE IS NO SUCH OPTION')

"""def choose_picture():
    decision = input("How do you like this picture?\n")
    options = ["Pretty", "Ugly", "Masterpiece - save!"]
    
def print_menu(menu_commands):

    for option in menu_commands:
        print(str(menu_commands.index(option)) + '----->' + option)

    if decision """

lista = ["s","s","s","s","s","s","s","s","s","s","s","s""s","s","s"]

print("".join(lista))
list_to_display = lista


