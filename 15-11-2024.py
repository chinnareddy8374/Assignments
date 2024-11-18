#  STRINGS 
# string is a collection of charactors.
# string is immutable.

#ex:-

message="Hai good morning!"
index=0
for i in message:
    print("message[",index,"]= ", i)
index += 1

#concatenate two strings.

str1 = "Hai good morning"
str2 = "hyderabad"
str3 = str1 +" "+ str2
print(str3)

# write a porgram to append a string using assignment oprerators.
srt1 = "hello"
name = input(  "\n Enter your name: ")
str1 += " "+ name
str1 += " "+ "welcome to python programming"
print(str1)

print('---------------------------------------------------------------------')

# string slicing :-

x= "welcome to India"
print(len(x))
print(x[13])
print(x[-10])
print(x[0:10])

print(x[-5:-11])

print(x[-11:-5])

print(x[10:5])

print(x[5:10])

print(x[1:10:2])

print(x[-15:-1:-3])


# string methods:-

x= input("Enter a word or sentence: ")
print("uppercase - ", x.upper())

print("lowercase - ", x.lower())

print("title - ", x.title())

print("count - ", x.count("p"))

print("split - ", x.split())
print(type(x))

#1. Python Program to count occurrence of a given characters in string. 

str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
print(d)


#2. Python Program to check if two Strings are Anagram. 
#ANAGRAM:-
# *Both strings shouid be of equal length.
# *Both strings should have same characters in same order or different order.

str1=input("Enter a string1: ")
str2=input("Enter a string2: ")
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    if sorted(str1) == sorted(str2):
        print("strings are Anagram")
    else:
        print("Not Anagram")


#3. Python program to check a String is palindrome or not. 
#palindrome:-
#if any string after reversing if i get same string that is called palindrome string.
sp=input("Enter a string: ")
revstr=(sp[::-1])
if revstr==sp:
    print("string is palindrome")
else:
    print("string is not palindrome")

#4. Python program to replace the string space with a given character. 
s="python"
c= "open source program"
s1=" "
for i in s:
    if i==" ":
        s1+=c
    else:
        s1 += i
print("string: ",s1)

#5. Python program to replace the string space with a given character using replace() method. 
str5="Replace space in this string"
replacement_char = "-"
output_string = str5.replace(' ', replacement_char)

print("original string: ", str5)
print("modified string: ",output_string)


#6. Python program to convert lowercase char to uppercase of string. 

s=input("Enter a string: ")
print(s.upper())

#7. Python program to check given character is digit or not using isdigit() method. 

sd=input("Enter a string: ")
print(sd.isdigit())


#8. Python program to separate characters in a given string. 
ss=input("Enter a string: ")
print(ss.split())

#9. Python program to remove blank space from string. 
ss1=input("Enter a string: ")
print(len(ss1))
ss2=(ss1.strip())
print(len(ss2))
print(ss2)

#10. Python program to concatenate two strings using join() method. 

sj1=input("Enter a string1: ")
sj2=input("Enter a string2: ")
js=" ".join([sj1,sj2])
print(js)

#11. Python program to concatenate two strings without using join() method. 

sc1=input("Enter a string1: ")
sc2=input("Enter a string2: ")
sc3=sc1+" "+sc2
print(sc3)

#12. Python program to remove repeated character from string. 
sr=input("Enter a string: ")
str=''
for ch in sr:
    if ch not in str:
        str=str+ch
print(str)

#13. Python program to count alphabets, digits and special characters. 
str13=input("Enter a string: ")
alphabets=0
digits=0
specialc=0
for ch in str13:
    if ch.isalpha():
        alphabets=alphabets+1
    elif ch.isdigit():
        digits=digits+1
    else:
        specialc=specialc+1
print("alphabets count: ",alphabets)
print("digits count: ",digits)
print("special chara count: ",specialc)

#14. Python program to check given character is digit or not. 
str14=input("Enter a string: ")
print(str14.isdigit())

#15. Python program to print all non repeating character in string. 
str15= input("Enter a string: ")
for i in str15:
    if str15.count(i)==1:
        print(i)


#16. Python program to copy one string to another string.  
str16=input("Enter a string: ")
p=(str16[:])
print(p)

#17. Python program to print the highest frequency character in a String. 
str17= "hello world"
max_char= max(set(str17),key = str.count)
print({f'highet frequenct char: {max_char}'})
print(f'frequency: {str.count,{max_char}}')

#18. Python program to calculate sum of integers in string.
str18="123456789"
total_sum=0
for i in str18:
    total_sum+=int(i)
print(total_sum)



#list:-
#list is a collection of data types. it holds the group of values
# list is a mutable object. 
#list allow duplicates.
#list can also created by using list() function.

#declaring a list:-
l=[1,2,3,4,5,6,7]
print(l)
print(type(l))

#mearging of two list:-
l1=[1,3,2,4,5,6]
l2=['a','b','c','d',]
print(l1+l2)
print(l1+l2+[7,8])

#loop in list:-
x=[1,2,3,4,5,6,7]
for p in x:
    print(p)
    print(type(p))

#nested list:-
nl=[["rohit",50],["sachin",150],["dhoni",100],["uvaraj",70]]
print(len(nl))
for p in nl:
    print(p)

for p,q in nl:
    print("player",p)
    print("runs",q)

NL=[1,'a',"abc",[2,3,4,5],8.9]
i=0
while i<(len(NL)):
    print("NL[",i,"]= ",NL[i])
    i+=1


#list functions:-

lf=[1,5,4,6,7,10,43,45,866]
print(sum(lf))
print(max(lf))
print(min(lf))
print(sorted(lf))
print(sorted(lf,reverse=True))

#list slicing:-
ls=["apple","banana","cherry","water melon","bag","fan","car","mobile","box","bottle"]
print(ls)
print(len(ls))
print(ls[2])
print(ls[-5])
print(ls[1:5])
print(ls[-8:-3])
print(ls[0:10:2])
print(ls[-10:-1:3])

#List Operation:-

#LEN():- Return length of list.
#ex:-
lo=[1,2,3,4,5,6]
print(len(lo))
print('-----------------------------')

#concatenation:- Join two lists.
#ex:-
lo1=["banana","apple"]
print(lo+lo1)
print('--------------------------')

#repetition:- Repeats elements in list.
#ex:-
print(lo1*2)
print('------------------------------')

#in:- checks if the value is present in the list.
#ex:-
print(4 in lo)
print('------------------------------')

print(10 in lo)
print('------------------------------')

#not in :-checks if the value is present in the list.
#ex:-
print(10 not in lo)
print('------------------------------')

print(4 not in lo)
print('------------------------------')

#max:- returns maximum value in the list.
#ex:-
print(max(lo))
print('------------------------------')

#min:- returns minmum value in the list
#ex:-
print(min(lo))
print('------------------------------')

# sum:-add the values in the list that has nubers.
# ex:-
print(sum(lo))
print('------------------------------')

# all:- returns true if all elements of list are true (or if the list is empty).
# ex:-
print(all(lo))
print('------------------------------')

# any:- returns true if any element of the list is true, if list is empty it returns false.
# ex:=-
print(any(lo))
print('------------------------------')

#list:- converts an iterable (tuple, string, set, dictionary) to a list.
# ex:-
list1=list("hello")
print(list1)
print('------------------------------')

#sorted:-returns a new sorted list.the original list is not sorted.
# ex:-
list2=[5,9,4,6,1,2]
list3=sorted(list2)
print(list3)
print('------------------------------')

#Write a program that forms a list of first character of every word in another list.
list_1=["hellow","wellcome","to","the","world","of","python"]
letters=[]
for word in list_1:
    letters.append(word[0])
print(letters)

#Write a program to create a list of numbers on the range 1 to 10 , then delete all odd numbers from the list and print the final list.

list_num=[]
for i in range(1,11):
    list_num.append(i)
print("original list: ", list_num)
for index, i in enumerate(list_num):
    if (i%2!=2):
        del list_num[index]
print("list after deletiong odd numbers: ", list_num)

#write a program to create a list of numbers in the specied range in particular steps.Reverse the list and print its values.
num_list=[]
m=int(input("Enter the starting of the range: "))
n=int(input("Enter the ending of the range: "))
o=int(input("Enter the step in the range: "))
for i in range(m,n,o):
    num_list.append(i)
print("Original list: ", num_list)
list_num.reverse()
print("Reversed list: ", num_list)

#write a program to create a list of fist 20 add numbers using the shortcut method.
odd=[2*i+1 for i in range(20)]
print(odd)

#Write a program to determine whether a person is eligible to vote or not . if he is not eligoble , display how many yers left to be eligible.
age=int(input("Enterthe age: "))
if(age>=18):
    print("your eligible to vote: ")
else:
    yers=18-age
    print("your have to wait for another" +" "+str(yers) + "yesrs to cast your vote")

#write a program to find larger of two numbers.
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
if(a>b):
    large=a
else:
    large=b
print("large=",large)



'''
Tuple:- tuple is a collection of data types, it holds the group of values

1)tuple allow dupleycates.
2)typle is immutable object.
3)tuple insection order is preaseved.
4)tuple created by using tuple()function.
5)tuple allow index.

'''

#creating a tuple:
t=(1,2,True,5.345,"hari",3,2,4,4)
print(type(t))
print(len(t))

#creating a tuple using tuple() function:
t1=tuple(input("Enter the values: "))
print(t1)
print(type(t1))
print(len(t1))

#converting tuple items:
t2=input("Enter the values: ")
print(t2)
print(type(t2))
t2_1=tuple(t2)
print(t2_1)
print(type(t2_1))

#accessing tuple:
t3=tuple(input("Enter the value: "))
print(type(t3))
print(t3[2])
print(t3[-4])

#tuple slicing:
t4=("apple","banana","watermellon","cherry","mango","kiwi",1,2,3,4,5.43,"q","A","D","Q")
print(t4[0:])
print(t4[:-1])
print(t4[5:10])
print(t4[-13:-8])
print(t4[2:14:3])
print(t4[-13:-1:2])
print(t4[::-1])
print(t4[-1:])

#Tuple using operators:
t5=("apple","banana","watermellon","cherry","mango","kiwi")
if "cherry" in t5:
    print("yes, its exist")
else:
    print("not exist")


if "kowshik" in t5:
    print("yes, its exist")
else:
    print("not exist")

#chang the tuple vales:
t6=("apple","banana","watermellon","cherry","mango","kiwi",1,2,3,4,5.43,"q","A","D","Q")
print(t6)
print(type(t6))

t6_1=list(t6)
t6_1[10]="Ravi"
print(t6_1)
print(type(t6_1))

t6=tuple(t6_1)
print(t6,type(t6))

t6_2=list(t6)
t6_2.remove("Ravi")
print(t6_2)

t6=tuple(t6_2)
print(type(t6))


#packing and unpacking:
marks=36,48,59,70,80
print(marks,type(marks))



# !)Write a program that counts the number of even and odd numbers in a list.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_count=0
add_count=0
for number in numbers:
    if number%2==0:
        even_count +=1
    else:
        add_count +=1
print("number of even numbers: ",even_count)
print("number of add numbers: ",add_count)

print('-----------------------------------------------------------------')

# 2)Write a program that prints the multiplication table for a given number.

n=int(input("Enter the value: "))
print("multiplication table of: ",n)
for i in range(1,11):
    print(n,'x',i,'=',n*i)

print('------------------------------------------------------------------')

# 3)Write a program to find the largest of three numbers using if statements.

number1=float(input("Enter The First Number: "))
number2=float(input("Enter The Second Number: "))
number3=float(input("Enter The third Number: "))
largest = number1
if number2>largest:
    largest= number2
if number3>largest:
    largest= number3
print("The Largest Number: ", largest)
print('------------------------------------------------------')

# 4)Write a program to calculate the factorial of a number using a for loop.

n=int(input("enter the value: "))
factorial=1
for i in range(1, n+1):
    factorial *=i
print(f"the factorial of{n} is {factorial}")

print('----------------------------------------------------------')

# 5)Write a program that takes a number as input and prints the sum of its digits. 

number=input("Enter the value: ")
sum_of_digit=0
for digit in number:
    sum_of_digit += int(digit)
print("the sum of digits is: ",sum_of_digit)

print('---------------------------------------------------------------')

# 6)Write a program that generates a random number between 1 and 100, and asks the user to guess it. The program should give hints ("too high" or "too low") until the user guesses correctly.

n = int(input("my gussing number is: "))
guess = None  
print("selecte the guess in number between 1 to 100")
while guess != n:
    guess = int(input("Guess a number:"))
    if guess<1 and guess>100:
        print(" guess a number between 1 and 100.")
    elif guess > n:
        print("Too high!")
    elif guess < n:
        print("Too low!")
    else:
        print("Correct!")

print('----------------------------------------------------------')

# 7)write a program to check if a number is an Armstrong number
n =int(input("enter a number:"))
temp=n
1==len(str(n))
sum=0
while(temp):
    r=temp%10
    sum=sum+r**1
    temp=temp//10
    print(sum)
if(sum==n):
    print("is a armstrong Number")
else:
    print("is not an Armstrong number")

print('----------------------------------------------------')

# 8)write a program to check if a string is a palindrome.
n=int(input("Enter a value: "))
temp=n
sum=0
while(n):
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)
print(n)
if(sum==temp):
    print("is a polindrome")
else:
    print("is not a polindrome")

print('----------------------------------------------')

# 9)write a program that check if a number is prime.

num =int(input("enter a number: "))
if num==1:
    print("not a prime number")
    if num>1:
        for n in range(2,num):
            if num%2==0:
                print(num, "is not a prime number ")
                break
            else:
                print(num, "num is a prime number")

print('-----------------------------------------------------------------')

# 10)Write a program that prints the numbers from 1 to 100. 
#For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". 
#For numbers which are multiples of both three and five, print "FizzBuzz".
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
