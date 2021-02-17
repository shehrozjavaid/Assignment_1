from functools import reduce
##T4

"""
Q1 Write a program to reverse a string.
    Sample input: “1234abcd”
    Expected output: “dcba4321”
"""
txt = input("Enter a string: ")
rev_txt= txt[::-1]

#################################
"""
Q2 Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
"""
def ustr_upper(str1):
    up, low = 0,0
    for i in str1:
        if i.isupper():
            up+=1
        elif i != ' ':
            low+=1
    print("No. of upper case chars: {}, No. of lower case chars: {}".format(up,low))
            
##################################

"""
Q3 Create a function that takes a list and returns a new list with unique elements of the first list.
"""
def lst_unique(lst):
    lst_u = set(lst)
    return list(lst_u)

####################################
"""
Q4 Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.
"""
in1= input("enter a hyphen-separated sequence of words: ")
in1=in1.replace('-','')
in1_sorted=sorted(in1)
for i in in1_sorted:
    print('{}-'.format(i),end='')
    
#####################################

"""
5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
"""
lines=list()
while True:
    line=input("Input a string or press enter to finish: ")
    if line:
        lines.append(line)
    else:
        break
input1 = '\n'.join(lines)
print(input1.upper())

#########################################
"""
6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.
"""
def string_summer(x,y):
    x=int(x)
    y=int(y)
    z=x+y
    return z

string_summer('1','2')

##########################################

"""
7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.
"""
def str_len(s1,s2):
    if len(s1)>len(s2):
        print(s1)
    elif len(s2)>len(s1):
        print(s2)
    elif len(s1)==len(s2):
        print(s1)
        print(s2)
str_len("this is a string","this is a longer string")    

####################################################

"""
8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included)
"""
def t_gen():
    l1=list()
    for i in range(1,21):
        l1.append(i)
    t1=tuple(l1)
    print(t1)

t_gen()

####################################################

"""
9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN
1 ODD
2 EVEN
3 ODD
"""
def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i,'EVEN')
        else:
            print(i,'ODD')

showNumbers(15)

####################################################

"""
10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)
"""
filtered_list= list(filter(lambda x1: x1%2==0,range(1,21)))

###################################################
"""
11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.
"""
filtered_list= list(filter(lambda x1: x1%2==0,range(1,21)))
squared_list= list(map(lambda x2: x2*x2,filtered_list))

##################################################
"""
12. Write a function to compute 5/0 and use try/except to catch the exceptions
"""
try:
    x=5//0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
##################################################
"""
Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
"""
flatten_list=reduce(lambda x,y: str(x)+str(y),[1,2,3,4,5,6,7])

##################################################
"""
14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.
"""
values=list(filter(lambda x:x%3!=0 and x%7==0,range(1,101)))

##################################################
"""
15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.
"""
def num_squared(l1):
    return l1*l1

squared_list=list(map(num_squared,[1,2,3,4,5,6]))
print(squared_list)

#################################################
"""
16. What is the output of the following codes:
    (i) def foo():
            try:
                return 1
            finally:
                return 2
        k = foo()
        print(k)
    (ii) def a():
            try:
                f(x, 4)
            finally:
                print('after f')
                print('after f?')
        a()
"""
##  Ans (i) 2
##  Ans (ii) ERROR f is not defined









