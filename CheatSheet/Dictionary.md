Items are ordered, changeable, and doesn't allow duplicate
duplicate value will overwrite existing value

Cteate dict
dict_example = {
    "key" : "value"
    "key1" : "value2"
}
print("key")    #"value"

dict() function
Empty_dict = dict(key = "value", key2 = 100)


Add / Change item to dict
dict_example = {
    "key" : "value"
    "key1" : "value2"
}
dict_example["newKey"] = "newValue"

dict_example["key1"] = "changedValue1"
dict_example.update({"key":ChangedValue})


Remove Item
dict_example = {
    "key" : "value"
    "key1" : "value2"
}
dict_example.pop("key1")
print(dict_example)     #{"key" : "value"}
dict_example.popitem()      removes the last inserted item

del dict_example["key"]     delete specified key and value
del dict_example            delete whole dict

dict_example.clear()        empty the dict


Check if key exists
if "key1" in dict_example:
    doSomeThing



Get value from dict
dict_example = {
    "key" : "value"
    "key1" : "value1"
}
x=dict_example = ("key")    #"value"

x=dict_example.get("key1")  #"value1"


Get list of the keys:
dict_example.keys()

Get list of the values:
dict_example.values()


LOOP
Print all key in the dictionary:
for x in thisdict:
  print(x)

Print all values in the dictionary:
for x in thisdict:
  print(thisdict[x])

return values of a dictionary:
for x in thisdict.values():
  print(x)

return keys of a dictionary:
for x in thisdict.keys():
  print(x)

Loop through both keys and values, using items() method:
for x, y in thisdict.items():
  print(x, y)


dict_example.copy()     copy the whole dict

Nested Dictionary
Nest_Dict = {
  "Dict1" : {
    "key1_1" : "value1_1",
    "key1_2" : 1.2
  },
  "Dict2" : {
    "key2_1" : "value2_1",
    "key2_2" : 2.2
  },
  "Dict3" : {
    "key3_1" : "value3_1",
    "key3_2" : 3.2
  }
}



Dict1 = {
    "key1_1" : "value1_1",
    "key1_2" : 1.2
}
Dict2 = {
    "key2_1" : "value2_1",
    "key2_2" : 2.2
}
Dict3 = {
    "key3_1" : "value3_1",
    "key3_2" : 3.2
}
Nest_Dict = {
    "Dict1" : Dict1,
    "Dict2" : Dict2,
    "Dict3" : Dict3
}

Access item in Nested Dict
print(Nest_Dict["Dict3"]["key3_2"])


LOOP through
for x, obj in Nest_Dict.items():
    print(x)                        #print dict name

    for y in obj:
        print(y + ':', obj[y])      #print keys and values


Method	                Description
clear()	        Removes all elements 
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates with the specified key-value pairs
values()	    Returns a list of all the values