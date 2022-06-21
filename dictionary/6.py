dictionary_personal = dict(name="name",age="65",gender="male",phone=1234567890)
#using pop()
dictionary_personal.pop("age")
print(dictionary_personal)
#using popitem() remove last inserted item
print(dictionary_personal.popitem())
print("list now :{0}".format(dictionary_personal))