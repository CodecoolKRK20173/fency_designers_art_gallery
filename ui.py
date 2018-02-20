import sys
import os



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



def print_picture(picture):
    """
    Function that display generated picture.
    """

    LAVA = "▒"
    ROCK = "#"
    GROUND = "."
    GRASS = ","
    WATER = "░"
    GOLD_COIN = "©"
    TREE = "+"
    WOOD = "0"
    EAST_GATE = ">"
    SOUTH_GATE = "V"
    NORTH_GATE = "^"
    TOWN_GATE = "¤"
    CEMENTARY_NPC = "Ì"
    DRAGON_TP = "®"


    RED = "\033[1;31;40m"
    NORMAL = "\033[0m"
    WHITE = "\033[1;37;40m"
    DARK_GREY = "\033[1;30;40m"
    BRIGHT_CYAN = "\033[1;36;40m"
    GREEN = "\033[1;32;40m"
    DARK_GREEN = ""
    GOLD = "\033[1;33;40m"
    BRIGHT_BLUE = "\033[0;34;40m"


    game_board = []
    for element in map_game:
        game_board.append(element) # Appending items to game_board list.


    for y in range(len(game_board)):
        for x in range(len(game_board[y])):
            if game_board[y][x] == LAVA:
                sys.stdout.write(RED)

            elif game_board[y][x] == ROCK:
                sys.stdout.write(WHITE)

            elif game_board[y][x] == DRAGON_TP:
                sys.stdout.write(RED)

            elif game_board[y][x] == GROUND:
                sys.stdout.write(DARK_GREY)
            
            elif game_board[y][x] == GRASS:
                sys.stdout.write(DARK_GREY)

            elif game_board[y][x] == WATER:
                sys.stdout.write(BRIGHT_CYAN) 

            elif game_board[y][x] == GOLD_COIN:
                sys.stdout.write(GOLD)

            elif game_board[y][x] == TREE:
                sys.stdout.write(GREEN)

            elif game_board[y][x] == WOOD:
                sys.stdout.write(NORMAL)
            
            elif game_board[y][x] == SOUTH_GATE:
                sys.stdout.write(BRIGHT_BLUE)

            elif game_board[y][x] == NORTH_GATE:
                sys.stdout.write(BRIGHT_BLUE)
            
            elif game_board[y][x] == EAST_GATE:
                sys.stdout.write(BRIGHT_BLUE)

            elif game_board[y][x] == TOWN_GATE:
                sys.stdout.write(BRIGHT_BLUE)

            elif game_board[y][x] == CEMENTARY_NPC:
                sys.stdout.write(RED)    

            else:
                sys.stdout.write(NORMAL)

            print(game_board[y][x], end="")

        sys.stdout.write(NORMAL)
        print()


    pass