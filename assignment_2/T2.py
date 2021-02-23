
##Assignment 2

##  T2  ##

"""
Q1 1. Write a program in Python to perform the following operation:
    If a number is divisible by 3 it should print “Consultadd” as a string
    If a number is divisible by 5 it should print “Python Training” as a string
    If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
    
"""
num1 = int(input("Enter a number:"))
if num1%3==0 and num1%5==0:
    print("Consultadd - Python Training")
elif num1%3==0:
    print("Consultadd")
elif num1%5==0:
    print("Python Training")

#####################################

"""
Q2 Write a program in Python to perform the following operator based task:
    Ask user to choose the following option first:
    If User Enter 1 - Addition
    If User Enter 2 - Subtraction
    If User Enter 3 - Division
    If User Enter 4 - Multiplication
    If User Enter 5 - Average
    Ask user to enter two numbers and keep those numbers in variables num1 and num2
    respectively for the first 4 options mentioned above.
    Ask the user to enter two more numbers as first and second for calculating the average as
    soon as the user chooses an option 5.
    At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
    NOTE: At a time a user can only perform one action.
    
"""
print("Enter a number between 1 and 5\nEnter 1 - Addition\nEnter 2 - Subtraction\nEnter 3 - Division\nEnter 4 - Multiplication\nEnter 5 - Average")
choice_num = int(input("choice: "))
num1, num2 = input("Enter Two Numbers Seperated by space: ").split()
num1,num2 = int(num1),int(num2)
if choice_num in [1,2,3,4]: 
    if choice_num==1: 
        print("{} + {} = {}".format(num1,num2,num1+num2))
        if num1+num2<0: print("NEGATIVE")
    if choice_num==2: 
        print("{} - {} = {}".format(num1,num2,num1-num2))
        if num1-num2<0: print("NEGATIVE")
    if choice_num==3: 
        print("{} / {} = {}".format(num1,num2,num1//num2))
        if num1//num2<0: print("NEGATIVE")
    if choice_num==4: 
        print("{} * {} = {}".format(num1,num2,num1*num2))
        if num1+num2<0: print("NEGATIVE")
elif choice_num==5:
    first,second = input("Enter Two more number for average separated by space: ").split()
    first,second = int(first),int(second)
    print("Average of {} {} {} {} is {:.2f}".format(num1,num2,first,second,(num1+num2+first+second)/4))
    

#######################################

"""
Q3 Write a program in Python to implement the given flowchart:  
"""

a,b,c = 10,20,30
avg = (a+b+c) /3
print("avg = {:.2f}".format(avg))
if (avg>a and avg >b and avg > c):
    print("avg is higher than a,b,c")
elif avg>a and avg>b: print ("avg is higher than a,b")
elif avg>a and avg>c: print ("avg is higher than a,c")
elif avg>b and avg>c: print ("avg is higher than b,c")
elif avg>a: print ("avg is just higher than a")
elif avg>b: print ("avg is just higher than b")
elif avg>c: print ("avg is just higher than c")

########################################

"""
Q4 Write a program in Python to break and continue if the following cases occurs:
    If user enters a negative number just break the loop and print “It’s Over”
    If user enters a positive number just continue in the loop and print “Good Going”
"""
while(1):
    num1=int(input("Enter a number: "))
    if num1>0:
        print("Good Going!")
        continue
    else:
        print("Game Over!")
        break

########################################    

"""
Q5 Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.
"""
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i)
    
#######################################

"""
What is the output of the following code examples?

x=123
for i in x:
    print(i)

Ans: Error: Int is not iteratable
###################
i=0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print(“error”)

Ans: 
0 
error
1
error
2
#####################
count=0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break

Ans: 
0
1
2
3
4
Error 'Break' is not defined use 'break'

"""

#######################################
"""
Q7 Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement
"""
for i in range(0,7):
    if i==3 or i==6:
        continue
    else:
        print(i,end=' ')

######################################

"""
Q8 Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2
"""
str_input = input("Enter a string: ")

Letters,Digits = 0,0
for i in str_input:
    if i.isdigit():
        Digits+=1
    elif i.isalpha():
        Letters+=1
    else:
        pass    
print("Letters {} Digits {}".format(Letters,Digits))

######################################

"""
Q9
Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.

Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)
"""
'''
Part1:
    
lucky_n = 7
while(1):
    x=int(input("Guess the lucky num: "))
    if x==lucky_n: 
        break
    else:
        continue
'''        
#Part2

lucky_n = 7
while(1):
    number=int(input("Guess the lucky num: "))
    if number==lucky_n: 
        break
    else:
        answer=input("continue..?(Yes/No): ")
        if(answer=="Yes"):
            continue
        elif(answer=="No"):
            break
        
###########################################

"""
Q10 Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
    count=1
    While counter <= 5:
        print(“Type in the”, counter, “number”
        counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.
"""          
count=1
lucky_num=7
while count<=5:
    number=int(input("Guess the lucky num: "))
    if number==lucky_num:
        print("Good guess!")
    else:
        print("Try again")
    count=count+1    
print("Game over!")

###########################################################

"""
Q11 In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.
"""

count=1
lucky_num=7
while count<=5:
    number=int(input("Guess the lucky num: "))
    if number==lucky_num:
        print("Good guess!")
        break
    else:
        print("Try again")
    count=count+1   
if number!=lucky_num:
    print("Sorry but that was not very successful")























