import pathlib
import os
filename = input("\nPlease enter a file name:")
path = str(pathlib.Path(__file__).parent.resolve())
path+="\{0}".format(filename)
if(os.path.exists(path)):
    print("File  exists opening  file.....\n")
    filehandler = open(path,'at')
    data =input("\n enter you data to write:\n")
    filehandler.write(data)
    filehandler.close()
else:
    print("File not exists creating file.....\n")
    filehandler = open(path,'at')
    data =input("\n enter you data to write:\n")
    filehandler.write(data)
    filehandler.close()
