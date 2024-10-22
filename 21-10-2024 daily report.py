#FUCTION:-
# A Fuction is a block of statement which performs perticular task.
# ex:- print(),type(),len(),id(),roud(),int().etc
# Functions are not executed automatically.
# To executed functions, we need to make a function call.
# we defined a fuction by using a keyword 'def'
# Function define once but can call for multipule times
# we can not call the a function before its definition.

#Examples:-
def wish ():                    #Function definition
    print("hello")
    print("Good Morning")
wish()                          #Function call



def add():                      #Function to add two numbers
     x=int(input("Enter the value of x : "))
     y=int(input("Enter the value of y : "))
     z=x+y                       #Function name assigned to a variable
     print("sum = ", z)
add()



def display():
    print("hello")
display()
display()
display()
display()
display()
display()
display()



def english():
    print("a,b,c,d,e,f,g,.....................")
def maths():
    print("1,2,3,4,5,6,....................")
def chemistry():
    print("h2o is chemical name of water")
maths()
chemistry()
english()



def diff(x,y):                  #Function to add two numbers
    return x-y
a=2035
b=2334
operation = diff                #Function name assigned to a variable
print(operation(a,b))           



def func():
    for i in range(4):
        print("hello word")
func() 



def func(i):
    print("hello world",i)
func(5+2*3)



def total(a,b):
    result=a+b
    print("sum of", a, "and", b, "=", result)

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
total(a,b)