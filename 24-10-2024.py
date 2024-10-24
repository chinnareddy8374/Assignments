# Modules:- Python modules are files containing python code that defines function, calss,, and variables.
 
#Built-in modul:-
 
#math module: The math module offers mathematical functions used for advanced arithmetic operations. This includes trigonometric functions, logarithmic functions, and constants like pi and e. This module is used to perform complex calculations using Python program.
 
#Ex:-
import math
sqrt_val = math.sqrt(64)
pi_const = math.pi
print(sqrt_val)
print(pi_const)
 
#datetime module:- The datetime module allows for manipulation and reading of date and time values. Some of the basic method of “datetime” module are “datetime.date”, “datetime.time”, “datetime.datetime”, and “datetime.timedelta”.
 
import datetime
 
print(dir(datetime))
 
#Ex:-
 
date_today = datetime.date.today()
time_now = datetime.datetime.now().time()
print(date_today)
print(time_now)
 
#Random Module:- The random module in Python is used to generates random numbers and provides the functionality of various random operations such as ‘random.randint()’, ‘random.choice()’, ‘random.random()’, ‘random.shuffle()’ and many more.
 
#Ex:-
 
import random  
num = random.randint(1, 10)
print(f"Random integer between 1 and 10: {num}")
fruits = ["Java", "C", "C++", "Python"]
chosen_fruit = random.choice(fruits)
print(f"Randomly chosen language: {chosen_fruit}")
 
#functool module:- which is included in Python's standard library, provides essential functionality for working with high-order functions
 
#Ex:-
 
from functools import reduce
list1 = [2, 4, 7, 9, 1, 3]
sum_of_list1 = reduce(lambda a, b:a + b, list1)
 
list2 = ["abc", "xyz", "def"]
max_of_list2 = reduce(lambda a, b:a if a>b else b, list2)
 
print('Sum of list1 :', sum_of_list1)
print('Maximum of list2 :', max_of_list2)