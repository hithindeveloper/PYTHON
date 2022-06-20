list = [1,2,3,4,5,6,7]
list_even=[]
list_odd=[]
for x in list:
    if(x%2==0):
        list_even.append(x)
    else:
        list_odd.append(x)
message_even="Even List {0}".format(list_even)
message_odd="Odd List {0}".format(list_odd)
print(message_even)
print(message_odd)