## T6

"""
1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.
"""
s="asDFsdrgvdSDGrR"
lst1=[x for x in s if x.isupper()]
print(lst1)


"""
2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
"""
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']

mydict = dict(zip(students,subjects))
print(mydict)


"""
3. Learn More about Yield, next and Generators
"""


"""
4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”
"""
def gen1(s):
    for c in s[::-1]:
        yield c
        
str1="Consultadd Training"

for i in gen1(str1):
    print(next(i))


"""
5. Write an example on decorators.
"""

def func1():
    print("inside original function")
func1()

def my_decorator(func):
    def inner_func():
        print("before func")
        func()
        print("after func")
    return inner_func

func1 = my_decorator(func1)

func1()


def hello_decorator(func): 
    def inner1(*args): 
          
        print("before Execution") 
          
        # getting the returned value 
        returned_value = func(*args) 
        print("after Execution") 
          
        # returning the value to the original frame 
        return returned_value 
          
    return inner1 
  
  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b,c): 
    print("Inside the function",a,b,c) 
    return a + b + c
  
a, b, c = 1, 2, 3
  
# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b,c))





