def export_to_file(filename, picture, mode = "a"):
    
    if mode == "w" or mode == "a":
        with open(filename+".txt", mode) as file:
            for line in picture:
                file.write("".join(line) + "\n")      
    else:
        raise ValueError("Wrong write mode")

def import_from_file(filename):

    with open(filename+".txt", "r") as file_list:

        lines = file_list.readlines()
    data = [color.replace("\n", "").split(",") for color in lines]

    return data