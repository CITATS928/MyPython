# Six basic data type
# Bool. Number, String, Tuple, List, Set, Dictionary
# Bool, Number, String, Tuple 属于不可变类型
"""
当分配了x=1之后，如果再分配x=2，会分配给x一个新的地址，
其他几个会直接给原地址抹掉重新赋值
"""

#Bool
true = True
false = False
string = "Hello World"
print(string.isalnum()) #-->is all number
print(string.isalpha())
print(string.isupper())
# Fasle*3


#Number
#Number datatype int, long, float, complex
a, b, c, d = True, 20, 5.5, 4+3j
print(type(a), type(b), type(c), type(d))
# <class 'bool'> <class 'int'> <class 'float'> <class 'complex'>
number = 0xA0F # Hax
print(number) # 2575
number = 0o37 # Octal
print(number) # 31

print(3 / 2) # return a float
print(4 // 2) # return an integer
print(3 % 2) # Modulo
print(3 ** 2) # Exponentiation
print(3*0.1)


#String
str1,str2,str3 = "A", "B","C"
print(str1+str2+str3)   #-->ABC
first_name = "qi"
last_name="wa"
full_name = f"{first_name} {last_name}" #qi wa    f-format
full_name2 = f"{first_name.upper()} {last_name.upper()}" #QI WA
print(full_name)
print(full_name2)


