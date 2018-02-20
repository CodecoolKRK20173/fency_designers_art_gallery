import display
import ui

def choose():

    inputs = input("Please enter a number: ")
    option = inputs[0]
    if option == "1":
        login = input("Login: ")
        password = input("Password: ")
        ui.login
    elif option == "2":
         
    elif option == "3":
         
    elif option == "4":
 
    elif option == "5":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():

    options = ["Login",
               "Register",
               "Show me gallery",
               "About",
               "Exit program"]
               
    display.print_menu("Main menu", options)

def main():
    screen.hello_screen()
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            print(err)

    main()
