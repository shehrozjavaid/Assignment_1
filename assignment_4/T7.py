# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:17:15 2021

@author: Shehroz Javaid
"""

"""
1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.
"""
import math

def formula_fun(D):
    C=50
    H=30
    for d in D:
        d=int(d)
        q=2*C*d    
        Q=math.sqrt(q//H)
        print(Q)
        
D=input("Enter comma seperated values of D: ").split(',')
formula_fun(D)

#######################################
"""
2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.
"""
class Shape:

    def area(self):
        print("default area is:",0)
        
class Square(Shape):
    def __init__(self,l):
        self.len_1=l
    
    def area(self):
        print("area of square is:",self.len_1**2)


a=Shape()
a.area()

s=Square(5)
s.area()

#########################################
"""
3. Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]
"""

class sum_2_zero:
    def __init__(self,a):
        self.arr=a
        
    def find_sum(self):
        n=len(self.arr)
        r=list()
        for i in range(0,n-1):
            s=set()
            for j in range(i+1,n):
                x=-(self.arr[i]+self.arr[j])
                if x in s:
                    #print(x,self.arr[i],self.arr[j])
                    r.append([x,self.arr[i],self.arr[j]])
                else:
                    s.add(self.arr[j])
        
        return r
 
a=[-25,-10,-7,-3,2,4,8,10]
obj1=sum_2_zero(a)
print(obj1.find_sum())

############################################
"""            
4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute.     
"""            

class Time:
    def __init__(self,h,m):
        self.hours=h
        self.minutes=m
        
    def addTime(self,obj1,obj2):
        h=obj1.hours+obj2.hours
        m=obj1.minutes+obj2.minutes
        if m>60:
            m-=60
            h+=1
        print("{} hr and {} min".format(h,m))
    def displayMinute(self):
        print(self.minutes+(self.hours*60),"minutes")
        
        
t1=Time(2,50)
t2=Time(3,32)
t2.addTime(t1, t2) 
t2.displayMinute()
     
###############################################
"""
5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:
    yearPasses() should increase age by the integer value that you are passing inside the function.
    amIOld() should perform the following conditional actions:I
        f age is between 0 and <13, print “You are young”.
        If age is >=13 and <=19 , print “You are a teenager”.
        Otherwise, print “You are old”.
"""

class Person:
    def __init__(self,age):
        if age>0:
            self.age=age
        else:
            self.age=0
            print("Age not valid, setting age to 0")
            
    def yearPasses(self,n):
        self.age+=n
        print(self.age)
    def amIOld(self):
        if self.age in range(0,13):
            print("you are young")
        elif self.age in range(13,20):
            print("You are a teenager")
        else:
            print("you are old")

a=Person(16)
a.yearPasses(4)
a.amIOld()





















       
            
            
            
            
            







        