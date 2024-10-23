#Default argument : These allow you to set default values for parameters. If no value is provided, the default is used.

#Ex:-

def myFun(x, y=30):
    print("x: ", x)
    print("y: ", y)

myFun(60)


#Keyword Arguments: Passing values by their names. 

#EX:-

def greet(arg_1, arg_2): 

    print(arg_1 + " " + arg_2) # Good Morning chinna reddy

greet(arg_1="Good Morning", arg_2="chinna reddy") 

#Positional Arguments: Values can be passed without using argument names. These values get assigned according to their position. Order of the arguments matters here. 

#Ex:-

def greet(arg_1, arg_2): 

    print(arg_1 + " " + arg_2) # Good Morning chinna reddy 

greeting = input() # Good Morning 

name = input() # chinna reddy

greet(greeting, name) 

#Variable-length Arguments: a feature that allows a function to accept a variable number of arguments in Python.

#Ex:-

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'Skywaves')







#1. Write a Python function to check whether a number falls within a given range.
def check_range(n):
    if n in range(1,20):
        print("yes, the number within range")
    else:
        print("out of range")
check_range(19)

#2. Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

def count_letters(c):
    d={"Upper_case":0, "Lower_case":0}
    for s in c:
        if s.isupper():
            d["Uppwe_case"] +=1
        elif s.islower():
            d["Lower_case"] +=1
        else:
            pass
    print("Original string", c)
    print("no.of upper case characters : ",d["Upper_case"])
    print("no of Lower case characters : ",d["Lower_case"])
    count_letters('The quick Brow Fox')

#3. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique_elements(e):

    u=[]
    for i in e:
        if i not in u:
            u.append(i)
    print(u)
e=[1,2,3,3,3,3,4,5]
unique_elements(e)

