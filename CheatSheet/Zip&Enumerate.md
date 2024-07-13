Zip
1. A function that takes two or more sequences and interleaves them.
2. return a zip object

Example:
s = 'abc'
t = [0, 1, 2]
result = zip(s, t)
type(result)        # <class 'zip'>

Iterating with zip
s = 'abc'
t = [0, 1, 2]
for pair in zip(s, t):
    print(pair)

# ('a', 0)
# ('b', 1)
# ('c', 2)



Enumerate

Example:
trilogy = ['The Matrix', 'The Matrix Reloaded', 'The Matrix Revolutions']
for index, element in enumerate(trilogy, start= 1):
    print(index, element)

# 1 The Matrix
# 2 The Matrix Reloaded
# 3 The Matrix Revolutions