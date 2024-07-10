# Class1.py
# Perform simple math expressions with numbers
num1 = 10
num2 = 5

kris = 'kris'

# Addition
result_add = num1 + num2
print("Addition:", result_add)

# Subtraction
result_sub = num1 - num2
print("Subtraction:", result_sub)

# Multiplication
result_mul = num1 * num2
print("Multiplication:", result_mul)

# Division
result_div = num1 / num2
print("Division:", result_div)

# Modulo
result_mod = num1 % num2
print("Modulo:", result_mod)

# Exponentiation
result_exp = num1 ** num2
print("Exponentiation:", result_exp)

# Declare and initialize a variable
name = "ZipCode"

# Print the value of the variable
print("Hello, " + name + "!")

# Declare and initialize a list
numbers = [1, 2, 3, 4, 5]

for x in range(10):
    print(x)

# Iterate over the list using a for loop
for num in numbers:
    # Print each number in the list
    print("Number:", num)

# Declare and initialize a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Iterate over the dictionary using a for loop
for key, value in person.items():
    # Print each key-value pair in the dictionary
    print(key + ":", value)


# Define a simple function that adds two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Call the function and print the result
result = add_numbers(3, 4)
print("Result of addition:", result)

# Define a simple function that multiplies two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

# Call the function and print the result
result = multiply_numbers(2, 5)
print("Result of multiplication:", result)

# Define a simple function that calculates the square of a number
def square_number(num):
    return num ** 2

# Call the function and print the result
result = square_number(6)
print("Result of squaring:", result)


####################################################

x,y = 8,9
a,b="string","txt"

print(x+y)
print(a+b)
#print(a+x) #----->Error TypeError: can only concatenate str (not "int") to str
print(type(x)) #---> <class 'int'> state what type of that varible  



