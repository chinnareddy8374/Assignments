                   

#1.write a program to print the number from 1 to 100


for i in range (1,100):
          print(i)

#2.For multiples of three ,print 'fizz' instead of the number and for multiple of five ,print 'buzz
for i in range(1,100+1):
    if(i%3==0):
        print("fizz")
    elif(i%5==0):
     print("buzz")
    else:
        print(i)  
 
 #3.For numbers which are multiples of both three and five ,print 'fizzbuzz"
for i in range (1,100+1):
    if(i%3==0 and i%5==0):
     print("fizzbuzz")
    else:
        print(i)  

#4.write a program that check if a number is prime
num =(input("enter a number: "))
if num==1:
    print("not a prime number")
    if num>1:
        for n in range(2,num):
            if num%2==0:
                print(num, "is not a prime number ")
                break
            else:
                print(num, "num is a prime number")


 # 5.write a program to check if a string is a palindrome.
n="madam"
rev=""
temp=n 
for i in n:
    rev=i+rev
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")

#6.write a program that generates a random number between 1 and 100and ask the user to guess it . the program should give hints('too low and too high) until the user guesses correctly

number_to_guess =45
attempts = 3

print("welcome to the number guessung game: ")
print("i'm thinking of a number between 1 and 10. an you guess it")
while attempts > 0:
    guess =int(input("enter your guess: "))

    if guess == number_to_guess:
        print("congratulations! you gussed the currect number!")
        break
    elif guess < number_to_guess:
        print("too low!")
    else:
        print("too high!")
    attempts -=1
    print(f"you have{attempts} attempts left.\n")

if attempts == 0:
    print(f"sorry,you've run out of attempts. the number was {number_to_guess}.")

print('-------------------------------------------------------------------')

    
#7.write a program that takes a number as input and print the sum of its digits
n=int(input("enter a number:"))
digits = 0
digit_sum = 0
temp = n  
while temp > 0:
    digit = temp % 10  
    digit_sum += digit  
    digits += 1         
    temp //= 10         
    print(digits)
    print(digit_sum)

#8.write a program to calculate the factorial of a number using a for loop
n=int(input("enter a number:"))
fact=1
for i in range (1,n+1):
    fact=fact*i 
    print(fact)

#9.write a program to find the largest of three number using if statement
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print("return n1")
elif(n2>n1 and n2>n3):
    print("return n2")
else:
    print(n3)  

 #10.write a program to check if a number is an Armstrong number
n =int(input("enter a number:"))
num=n
s=0
while n>0:
    r=n%10
s=s+r*r*r
n=n//10
if s==num:
    print(num," Armstrong number")
else:
    print(num, "Not an Armstrong")


#11.write a program that prints the multiplications table for given number
n=int(input("enter a number:"))
for i in range(1,11):
    print(n,'x',i,'=',n*i) 


#12.write a program that counts the number of even and odd number in list
n = [22,55,77,99,100,11,33,55]
even_count = 0
even_number=[]
odd_count = 0
odd_number=[]
for i in n:
    if i % 2 == 0:
        even_number.append(i)
    even_count += 1  
else:
    odd_number.append(i)
    odd_count += 1 
    print(even_count)
    print(even_number)
    print(odd_number)
    print(odd_count)
        
    