import ui
import os
import accounts


class bcolors:
    RED = "\033[1;31;47m"
    END = '\033[0m'
    

def print_magic_menu(menu_commands, indexx, title):
    os.system('clear')
    print (title)
    for option in menu_commands:
        if indexx == menu_commands.index(option):
            print(bcolors.RED + option + bcolors.END)
        if indexx != menu_commands.index(option):
            print(option)


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get_input(i, menu_commands):
    accept = 0
    option = getch()
    print(option)
    if option == 'w':
        if i > 0:
            i -= 1
    if option == 's':
        if i < len(menu_commands) - 1:
            i += 1
    if option == 'f':
        accept = 1
    return i, accept

