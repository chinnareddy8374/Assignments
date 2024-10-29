#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"

def wish():
    greet="hello" 
    name= input("Enter a name here : ")
    print(greet +' '+ name)
wish()
#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.

def add():
    num_1 = int(input("Enter The Number_1 Here : "))
    num_2 = int(input("Enter The Number_2 Here : "))
    total = num_1+num_2
    print("sum = ", total)
add()


#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.

def is_even(number):
    if number%2==0:
        return "True"
    else:
        return "Flase"
num = int(input("Enter a number : "))
result = is_even(num)
print(f"the number {num} is {result}.")


#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).

def factorial(c):
    if c==1 or c==0:
        return 1
    else:
        return (c*factorial(c-1))
c = int(input("entr the value : "))
result= factorial(c)
print("factorial of ", c,"is : ", result)


#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.

def max_of_three(a,b,c):
    return max(a,b,c)
a=22
b=45
c=39
operation = max_of_three
print(max_of_three(a,b,c))


#6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
            return count
result = count_vowels("python is easy")
print(result)  

#7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

def is_prime(num):
    num=int(num)
    if num>=0 and num%2==0:
        print("yes,it's prime")
    else:
        print("no,it's not a prime")

num=input("Enter a value : ")
is_prime(num)
#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def sum(n):
    if n<=1: 
        return n
    return n + sum(n-1)
n = int(input("Enter a Number Here : "))
print(sum(n))

#9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.

def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

print("select Operation")
print("1.addition"\
      "2.subtraction"\
      "3.multiplication"\
      "4.dividion\n")

operation=int(input("Enter choice of operation 1/2/3/4 : "))

n1=float(input("Enter n1 value : "))
n2=float(input("Enter n2 value : "))

if operation==1:
    print(n1,"+",n2,"=",addition(n1,n2))
elif operation == 2:
    print(n1,"-",n2,"=",subtraction(n1,n2))
elif operation == 3:
    print(n1,"*",n2,"=",multiplication(n1,n2))
elif operation == 4:
    print(n1,"/",n2,"=",division(n1,n2))
else:
    print("invalied value")


#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.

def elements(a,b):
    a= set(a)
    b= set(b)

    if (a & b):             # Intersection : it returns common elements in both sets.
        print(a & b)
    else:
        print("No Common Elements")

a=list(input("Enter a Value_1 Here : "))
b=list(input("Enter a Value_2 Here : "))
elements(a,b)

#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
def reverse(s):
    return s[::-1]
str=input("Enter a word or sentence :")
print("Reverse string : ",reverse(str))




