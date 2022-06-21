import pathlib
filename = input("\nPlease enter a file name:")
path = str(pathlib.Path(__file__).parent.resolve())
path+="\{0}".format(filename)
#a mode used to create a file in append mode if file exists it append the content to the file
filehandler = open(path,"a")
filehandler.close()