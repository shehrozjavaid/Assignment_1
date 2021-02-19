##Extra_task

from functools import reduce

"""
1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list: [1, 2, 3, 4]Access list: [600, 700]
Access list: [100, 300, 500, 600, 800]
Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list: [10]
Access list: [ ]
"""
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

access_list1=x[5][0:4]
access_list2=x[6:]
access_list3=[list(x[::-1])]
access_list4=[x[5][5][0]]

"""
2. Create a list of thousand numbers using range and xrange and see the difference between each
other.
"""
list_thousand=range(1,1001,1)
#list_thousand=xrange(1,1001,1)

"""
3. How Tuple is beneficial as compared to the list?
"""

#   Ans: Tuples are immutable so its faster to iterate through them and they use less memory

"""
4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2
"""
x1=range(1,101)
for i in x1:
    if i%3==0 and i%2==0:
        print(i)

"""
5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.
"""
x=input("Enter a string: ")
x_rev=x[::-1]
x_rev_vows=""
for c in x_rev:
    if c in 'aeiouAEIOU':
        x_rev_vows+=c
        
print(x_rev_vows)


"""
6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.
"""
var1="hello my name is abcde"
lst1=var1.split(' ')
for i in lst1:
    if len(i)%2==0:
        print(i)

"""
7. Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
"""

x=[1,2,3,4,5,6,7,8,9,-1]

for i in x:
    for j in x[x.index(i)+1:]:
        if i+j==8:
            print(i,j)
            

"""
8. Write a program in Python to complete the following task:
    Create two lists such as even_list and odd_list
    Ask user to enter a number in the range of 1,50 and make sure if the entered number is
    even, append it to the even_list and if the entered number is odd append it to the odd_list.
    Keep that in mind you can only add 5 items in each list
    Make sure once you enter all the 5 elements, calculate the sum of the list and return the
    maximum of the list.
"""
"""
even_list=list()
odd_list=list()
while((len(odd_list)<=5 and len(even_list)<=5)):
    n1=int(input("enter a number in the range of 1,50: "))
    if(n1%2==0):
        if(len(even_list)==5):
            print("Even list full!")
            continue
        else:
            even_list.append(n1)
    else:
        if(len(odd_list)==5):
            print("Odd list full!")
            continue
        else:
            even_list.append(n1)        
    

print("Sum of even_list:",sum(even_list),"Max of even_list", max(even_list))
print("Sum of odd_list:",sum(odd_list),"Max of odd_list", max(odd_list))
"""

"""
9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2
"""
lst1=list()
input1=input("enter a string: ")
for i in input1:
    if i not in "1234567890":
        lst1.append(i)
my_dict={i:lst1.count(i) for i in lst1}        
print(my_dict)

"""
10. Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).
"""
l1=list()
t1=(1,2,3,4,5,6,7,8,9,10)
for i in t1:
    if i%2==0:
        l1.append(i)
t2=tuple(l1)
print(t2)















































        