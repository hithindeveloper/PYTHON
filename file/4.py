import pathlib
import os
filename = input("\nPlease enter a file name:")
path = str(pathlib.Path(__file__).parent.resolve())
path+="\{0}".format(filename)
if(os.path.exists(path)):
    file_handler = open(path,'r')
    file_handler.seek(0)
    for x in file_handler.readlines():
        print(x,"\n")