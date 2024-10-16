#  STRINGS 
# string is a collection of charactors.
# string is immutable.

#ex:-

message="hello!"
index=0
for i in message:
    print("message[",index,"]= ", i)
index += 1

#concatenate two strings.

str1 = "hello"
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

