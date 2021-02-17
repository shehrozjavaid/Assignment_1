

##  T2  ##

"""
Q1 Create a list of 10 elements of four different data types like int, string, complex and float.
"""
x=['1',1,,complex(1+1j),1.0,2,3,4,5,9]

############################################

"""
2. Create a list of size 5 and execute the slicing structure
"""
y=[1,2,3,4,5]
y_slice=y[1:3]
 
#############################################
"""
3. Write a program to get the sum and multiply of all the items in a given list
"""
x=[1,2,3,4,5]
sum(x)
prod=reduce((lambda i,j: i*j),x)

##############################################
"""
4. Find the largest and smallest number from a given list
"""
x=[1,2,34,8,6]
x_max=max(x)
x+min=min(x)

###############################################
"""
5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list. 
"""
x1=[1,2,3,4,5]
x2=[]
for i in x1:
    if i%2==0:
        x2.append(i)
        x1.remove(i)
print(x2)

###############################################
"""
6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).
"""
l=list()
count=0
for i in range(1,31):
    count+=1
    if count<6 or count>25:
        l.append(i*i)
    
    else:continue    
print(l)

###############################################
"""
7. Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]
"""
lst=[1,3,5,7,9,10]
lst2=[2,4,6,8]
lst.pop()
lst.extend(lst2)
print(lst)
###############################################
"""
8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}
"""
a,b={1:10,2:20},{3:30,4:40}
a.update(b)
print(a)
##############################################
"""
9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
"""
n=int(input("Enter a number: "))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)

##############################################
"""
10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
"""
a=input('Enter a sequence of comma-separated numbers: ')
a=a.replace(",","")
l1=list()
for i in a:
    l1.append(i)
t1=tuple(l1)    
print(l1,t1)

##############################################


















    