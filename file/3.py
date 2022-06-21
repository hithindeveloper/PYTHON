import pathlib
import os
filename = input("\nPlease enter a file name:")
path = str(pathlib.Path(__file__).parent.resolve())
path+="\{0}".format(filename)
if(os.path.exists(path)):
    print("file exists do you want to contrinoue:1 for yes 2 no:\n")
    choice =int(input())
    match choice:
        case 1:
            os.remove(path)
            print("File removed")
        case 2:
            pass