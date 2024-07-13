List, mutable

List Operators
+	        List Concatenation
*	        List Repetition
in	        Element is a member of the sequence (bool)
not (in)	Element is not a member of the sequence (bool)





Nested List
stuff = [1, 'DOG', ['BALL', 'BAT']]
stuff[0]    #1
stuff[2]    #['BALL', 'BAT']
stuff[2][0] # 'BALL'
stuff[2][1] # 'BAT'



Slices
values = [1, 2, 3, 4, 5, 6]
values[1:4] = ['a', 'b', 'c']
print(values)       # [1, 'a', 'b', 'c', 5, 6]



List - Range of indexes
    list_example[start(included) : end(not included)]


List - Check if exists
    list_example = [1,2,3]
    if 1 in list_example:
        #True

List - Change item value
    list_example = ['a','b','c','d']
    list_example[1] = 'z'
    #['a','z','c','d']

    - Change Range
    list_example = ['a','b','c','d']
    list_example[1:3] = ['z','x']
    print(list_example)         #['a','z','x','d']

    list_example = ['a','b','c','d']
    list_example[1:3] = ['z']
    print(list_example)         #['a','z','d']


List Method - 
list.insert(position, input)
Example:
list_example = ["a", "b", "c"]
list_example.insert(2, "z")
print(list_example)     #['a', 'b', 'z', 'c']


list.append(input)
Example:
list_example = ["a", "b", "c"]
list_example.append("z")
print(list_example)     #['a', 'b', 'c', 'z']

list.extend(list_name) - will be added to the end of list. can be any iterable object (tuples, sets, dictionaries).
Eample:
list_example = ["a", "b", "c"]
added = ("z", "x", "c")
list_example.extend(added)
print(list_example)     #['a', 'b', 'c', 'z', 'x', 'c']



list.remove(input) - remove the first occurrence
Example
list_example = ["a", "b", "c", "b", "d"]
list_example.remove("b")
print(list_example)         #['a', 'c', 'b', 'd']


list.pop()
Example with index - pop the specified value out
list_example = ["a", "b", "c"]
list_example.pop(1)
print(list_example)     #['a', 'c']

Example withou index - pop the last item out
list_example = ["a", "b", "c"]
list_example.pop()
print(list_example)     #['a', 'b']

del list_example[index] or del list_example   (del whole list)
Example
list_example = ["a", "b", "c"]
del list_example[0]
print(list_example)     #['b', 'c']
del list_example
print(list_example)     #error


list.sort() - sory by alpha / number
Example:
list_example = ["z", "s", "b", "a", "k"]
list_example.sort()
print(list_example)         #['a', 'b', 'k', 's', 'z']

reverse a sort (z-a)
list_example = ["z", "s", "b", "a", "k"]
list_example.sort(reverse = True)
print(list_example)         #['z', 's', 'k', 'b', 'a']

customize sort function by key = function
Example: Sort the list by how close to 50:
def myfunc(n):
  return abs(n - 50)
list_example = [100, 50, 65, 82, 23]
list_example.sort(key = myfunc)
print(list_example)         #[50, 65, 23, 82, 100]

sort is case sensetive, upper case first, then lower case
Example to fix it:
list_example = ["banana", "Orange", "Kiwi", "cherry"]
list_example.sort(key = str.lower)
print(list_example)         #['banana', 'cherry', 'Kiwi', 'Orange']

list.sorted()   create a copy and sort
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)


list.reverse()
list_example = ["b", "a", "z", "x"]
list_example.reverse()
print(list_example)             #['x', 'z', 'a', 'b']


list.copy()
list1 = ["a", "b", "c"]
list2 = list1.copy()
print(list2)

list.clear()
list1 = ["a", "b", "c"]
list1.clear()


List - LOOP
loop through the list
list_example = ["a", "b", "c"]
for x in list_example:
  print(x)
    #a
    #b
    #c

loop through the list by index
list_example = ["a", "b", "c"]
for i in range(len(list_example)):
  print(list_example[i])

List Comprehension
[print(x) for x in list_example]

Syntax
List_comp = [expression for value in collection if condition]
 - condition can be optional
Ex: output= [str(value) for value in range(10) if value >5]

++++++






Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	        Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	        Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list