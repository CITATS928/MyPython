Tuple is immutable, but the changble item inside can be change.
items in tuple can be any type.

##Create tuple
1. tup = (4,5,6) 
2. built-in tuple function
    tup = tuple()
    ex. tup = tuple('string') #('s', 't', 'r', 'i', 'n', 'g')

nested_tup = (4, 5, 6), (7, 8)    #((4, 5, 6), (7, 8))

nested_tup[0]       #(4, 5, 6)

nested_tup[1]       #(7, 8)
nested_top[1][0]    #7


Tuples as return values
Example:
def first_and_last(word):
    return word[0], word[-1]

print(first_and_last("monkey"))
# ('m', 'y')


One item tuple:
thistuple = ("item",)



Check if exist
tuple = ("apple", "banana", "orange")
if "apple" in thistuple:
    #True

Add or Remove iteam in tuple:
change to list do the append or remove
        ex: x=("a","b","c")
        y=list(x)
        y[1]="d"
        x=tuple(y)
or
        x=("a","b","c")
        y=("d")
        x=x+y


Unpack Tuples
        Num_tup = (1,2,3)
        A,b,c = num_tup
        A #1
        B #2
        C #3

        Num_tup = (1,2,3,4,5,6)
        A,b,*c = num_tup
        A #1
        B #2
        C #(3,4,5,6)
        
with LOOP

loop through a tuple, Iterate through the items and print the values:

    tuple_example = (1,2,3,4)
    for x in tuple_example:
        print(x)
    #1
    #2
    #3
    #4

    tuple_example = (1,2,3)
    for i in range(len(tuple_example)):
        print(tuple_example[i])
    #1
    #2
    #3

    

Tuple count()method: return the number of timesa specified value occurs        tuple.count(parameter)
Example:
tuple_example = (1, 3, 5, 7, 7, 5, 3, 1, 5, 5)
x = tuple_example.count(5)
print(x)     #4


Tuple index() method: return the first position of the specified value.       tuple.index(parameter)
Example:
tuple_example = (1, 3, 5, 7, 7, 5, 3, 1, 3, 5)
x = tuple_example.index(7)
print(x)     #3
