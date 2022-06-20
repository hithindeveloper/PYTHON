number_list = [10,20,5,4,1,60]
search_number =int(input("Enter the number to search : "))
status = int(number_list.count(search_number))
if(status!=0):
    msg="Position is {}:"
    msg=msg.format(number_list.index(search_number))
    print(msg)

