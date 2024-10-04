#Guessing game 

number_to_guess =143
attempts = 5

print("welcome to the number guessung game: ")
print("i'm thinking of a number between 140 and 145. an you guess it")
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

# example for break, continue and pass statements
i=0
while i<10:
    i=i+1
    if(i==10):
        print("\n passing")
        pass
    if(i==5):
        print("\n continue")
        continue
    if(i==7):
        print("\n breaking")
        break
    print(i,end=" ")
print("\n done")

print('-----------------------------------------------------------------')

#example for forloop:-
# print a multiplication table 

n=int(input("enter the value: "))
print("multiplication table of",n)
for i in range(1,11):
    print(n,"X",i,"=",n*i)




