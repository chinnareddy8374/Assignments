#SET: set is a collection datatype which holds group of values.
# 1)Set represnted by using curly braces {}.
# 2)Set doesn't allow duplicates.
# 3)In set insection order is not preserved.
# 4)Set doen't suport indexing.
# 5)Set is a mutable object.
# 6)Set within a set is not allowed.
# 7)We can perform mathamatical operations on a set object.


# creating a set object:
s={10,20,30,40,50,"tata","jio","fan",(1,2,3,4)}
print(s)
print(type(s))

'''# accing set items by using for loop:
s1=set(input("Enter a values: "))
print(s1,type(s1))
print("apple" in s1)
'''
#set methods: 
# Add:
s2={"apple",1,2,3,3,"chinna"}
s2.add("fan")
print(s2,type(s2))

#Update:
s3={1,2,3,4,5,6,7,8,9,10}
s3_2={"powershell","car","tata","light"}
s3.update(s3_2)
print(s3)

#Copy :
s4={1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"light","tata","car","powershell"}
s4.copy()

# Remove :
s5={1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"light","tata","car","powershell"}
s4.remove("powershell")
print(s5)

# Discard :
s6={1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"light","tata","car","powershell"}
s6.discard("car")
print(s6)

# Pop :
s7={1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"light","tata","car","powershell"}
s7.pop()
print(s7)

# Write a quary to crate a set contaninig the first five prime numbers.
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

# how would you add the numbers 10 to set{2,3,5,7}.

s8={2,3,5,7}
s8.add(10)
print(s8)

# write a quary to remove the number 3 from the set{1,2,3,4,5}.

s9={1,2,3,4,5}
s9.remove(3)
print(s9)

# how can you check if the number 4 is in the set{1,2,3,4,5}.

s10={1,2,3,4,5}
if 4 in s10:
    print("yes, it exist")

# write quary to find the number of elements in the set{10,20,30,40,50}.
s11={10,20,30,40,50}
print(len(s11))
