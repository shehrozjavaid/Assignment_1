##Assigment_2

##  T1  ##

"""
Q1 Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
"""
a,b,c= 1,2.0,"this is a string"
print(a,b,c)

######################################

"""
Q2 Create a variable of type complex and swap it with another variable of type integer.
"""
v1_complex = complex(1+3j)
v2_int = 5
v1_complex,v2_int = v2_int, v1_complex
print(v1_complex,v2_int)

######################################

"""
Q3 Swap two numbers using a third variable and do the same task without using any third variable.
"""
n1=3
n2=6
temp1 = n2
n2 = n1
n1 = temp1
print(n1,n2)

######################################

"""
Q4 Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.
"""
input1 = input("Enter an input: ")
print(input1)

""" python 2 code
input2 = raw_input("Enter an input for python 2: ")
print input2
"""

######################################

"""
Q5 Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
"""
x,y = input("enter two numbers seperated by a space: ").split()
x,y=int(x),int(y)
z = x+y
result = z+30
print(result)

######################################

"""
Q6 Write a program to check the data type of the entered values.
"""
input3 = eval(input("enter a value: "))
print("The datatype of the value",type(input3))


######################################

"""
Q7 Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
"""
str_case = input("Enter a string: ")
str_camelCase_upper= str_case.title().replace(" ","")
str_camelCase_lower=str_camelCase_upper[0].lower()+str_camelCase_upper[1:]
str_snakeCase = str_case.replace(" ","_").lower()
str_upperCase = str_case.upper()

######################################

"""
Q8 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?

Ans: Yes because python doesn't declare variables, its a dynamically typed language'
"""





















