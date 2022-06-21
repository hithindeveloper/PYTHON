dictionary_personal = dict(name="name",age="65",gender="male",phone=1234567890)
#here we use keys to print data
for value in dictionary_personal:
    #using get()
    print("{0}={1}".format(value,dictionary_personal.get(value)),"\n")
    #using []
    print("{0}={1}".format(value,dictionary_personal[value]),"\n")
#here by help of values() we can directly access data in loop
for values in dictionary_personal.values():
    print(values,"\n")
    
#using items()
for key,value in dictionary_personal.items():
     print("{0}={1}".format(key,value),"\n")