def export_to_file(filename, picture):
    
    if mode == "w" or mode == "a":
        with open(filename+".txt", mode) as file:
            for line in albums:
                line = ','.join(line)
                file.write(line + "\n")          
    else:
        raise ValueError("Wrong write mode")

def import_from_file(filename):

    with open(filename+".txt", "r") as file:
        lines = file.readlines()
    data = [color.replace("\n", "").split(",") for color in lines]
    return data