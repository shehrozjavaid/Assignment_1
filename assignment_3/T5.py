## T6

"""
1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError
"""
try:
    x=0
    eval('x===x')
except SyntaxError:
    print("syntax error oppsie")
    
#################################################################

"""
2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.
"""
fname=input("enter file name to open: ")
try:
    f=open(fname, 'r')
except IOError:
    print("file does not exist!")
else:
    data = f.readlines() 
    for line in data: 
        word = line.split() 
        print (word)
    
#################################################################

"""
3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits” 
"""
try:
    i=input("Enter a number less than 4 digits long: ")
    assert len(i)<=4
except:
    print("“The length is too short/long !!! Please provide only four digits” ")
else:
    print(i)    
    
################################################################
    
"""
4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times
"""

Username='Shehroz'
Password='12345'
attempt=1
print("Please login")
u=input("UserName: ")
if u!=Username:
    print('Username not found')
elif u==Username:    
    while attempt<=3:
        p=input("Password: ")
        if p!=Password:
            attempt+=1
            print("Incorrect password try again!")
            continue
        else:
            print('login success')
            break
    if attempt>3:
        print("failed!")
        
#####################################################################

"""
5. Go through the link provided below to understand finally and raise concept:
https://www.programiz.com/python-programming/exception-handling
"""

####################################################################

"""
6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length

Make sure you return the content in The same link as it is present.
"""
with open('doc.txt','r') as f:
    for line in f:
        x=line.split(' ')
        if len(x)%2==0:
            print(line)









































