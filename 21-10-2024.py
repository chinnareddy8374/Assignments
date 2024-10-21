#TUPLE:-

#How do you create a empty tuple on python ?
t1=tuple()
print(t1,type(t1))

#Write a python program to unpack a tuple into several variables ?

t2=("apple","banana","mango","kiwi")
(s1,s2,s3,s4)=t2
print(s1)
print(s2)
print(s3)
print(s4)

#write a python program to add an item to the tuple ?

t3=("apple","lemon","apricot","plum","peaches","pears")
t3_1=list(t3)
t3_1.append("papayas")
t3=tuple(t3_1)
print(t3)

#Write a python proram to convert tuple into a string ?

t4=("apple","lemon","apricot","plum","peaches","pears")
str_1=str(t4)
print(str_1,type(str_1))

#DICTIONARY:-

#Write a python program to  add a key to a dictionary ?

dict1={"Brand":"Ford","Model":"Mustang","Year":1964}
dict1["color"]="red"
print(dict1)

#Write a python program to check weather the given value is present in the dictionary or not ?

dict2={"Brand":"Ford","Model":"Mustang","Year":1964}
if "Mustang" in dict2.values():
    print("Yes, it exist")
else:
    print("No, Not exist")

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict3={}
for x in range(1,16):
    dict3[x]=x**2
print(dict3)

#Write a python program to merge two python dictionaries ?

dict6={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30}
dict6_1={"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict6.update(dict6_1)
print(dict6)

#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

dict7={}
s="skywavessoftwares"
for letter in s:
    dict7[letter]=dict7.get(letter,0)+1
print(dict7)
