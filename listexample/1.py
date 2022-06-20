sample_list =[12, 35, 9, 56, 24]
messsage="Orignial {}".format(sample_list)
print(messsage)
lastindex=len(sample_list)-1
startindex=0
firstelement=sample_list[0]
lastelement=sample_list[lastindex]
sample_list[0]=lastelement
sample_list[lastindex]=firstelement
message="Modified{}".format(sample_list)
print(message)