list_numbers = [1,2,3,4,5,6]
msg = "You can remove from 0 to {0} positions".format(int(len(list_numbers)-1))
print(msg+"\n")
position = int(input("Please select a index :"))
list_numbers.remove(position)
print(list_numbers)