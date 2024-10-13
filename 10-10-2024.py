#1. Basic List Operations:
#1.Write a Python program to create a list of 5 integers and print the sum of all elements in the list.

lb=[1,2,3,4,5]
print(sum(lb))

#2.Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing.

lb_2=["banana","apple","cherry","water meoln","kiwi"]
print(lb_2[2])
print(lb_2[4])

#3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list.

lb_3=[1,2,3,4,5,6,7,8,9,10]
print(lb_3[0:3])
print(lb_3[-3:])
print(lb_3[1:11:2])


#2. Adding and Removing Elements:
#1.Write a Python program that initializes a list with some numbers:

l_a_r = list(range(1,7))
print(l_a_r)

#2.Adds a new number to the list using the append() method.

l_a_r.append(7)
print(l_a_r)

#3.Inserts a number at the second position using insert().

l_a_r.insert(1,7)
print(l_a_r)

#4.Extends the list with another list of numbers.

l_a_r_2=[10,9,8,7,6]
l_a_r_2.extend(l_a_r)

#5.Remove all occurrences of the number 3 from a list of integers.

print(l_a_r_2)
l_a_r_2.remove(3)
print(l_a_r_2)

#6.Write a Python program to remove the last element of a list using pop() and print the updated list.
l_a_r.pop()
print(l_a_r)



#3. Sorting and Reversing Lists:
#1.Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().

lsr = [1,7,3,6,2,0,8,9,6,5]

lsr.sort(reverse=True)
print(lsr)

lsr.sort()
print(lsr)


#2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.

lsr.reverse()
print(lsr)



#4. Aliasing and Cloning:
#1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.

l_a_c = [1,2,3,4,5,6,7,8,9]
x = l_a_c
print(x)

l_a_c.pop()
print(l_a_c)

print(x)

result = l_a_c.copy()


l_a_c.pop()
print(l_a_c)
print(result)


#2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.

l1 = [1,"a",2,"b"]
x = l1

l1.remove(2)
print(l1)
print(x)
print(id(x))
print(id(l1))


list = l1.copy()
print(list)

print(id(list))
print(id(l1))



#5. Mathematical Operations:
#1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.
l_m=[1,2,3,4,5]
l_m2=[6,7,8,9]

list=l_m + l_m2
print(list)


#2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).

l2 = []
for i in l_m:
   result = int(i) * 2
   l2.append(result)

print(l2)


#6. Membership Operators:
#1.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."

l_m = [1,2,3,4,5,6]
if 4 in l_m:
    result = l_m.index(4)
    print(result)
else:
    print("Element not found")



#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.

list = ["john","ranjitha","reethu","roshini","ramya","vandhana","sara"]


if "john" and "sara" in list:
    print("yes, both are There")



#7. Nested Lists:
#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
nl=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nl)):
    print(nl[i])
element=nl[1][2]
print(element)

#2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
nl2=[["reddy","A+"],["karthik","A"],["hari","B+"],["sandeep","B"],["siva","C"]]

for p,q in nl2:
    print("Name: ",p)
    print("Grade: ",q)



#8. Advanced Challenges:
#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers. 
#Another containing only the odd numbers.

l=[l for l in range (1,25+1)]
print(l)
even_num=[]
odd_num=[]
for i in l:
    if(i%2==0):
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)     


#2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).

la=[1,2,3,4,5,5,6,3,2,1,7,3,4,5]
la2=[]
for i in la:
    if i not in la2:
        la2.append(i)
print(la2)

#Given a list of tuples representing (name, age), sort the list by age in ascending order.
list_1=[("karthik",20),("venu",30),("hari",25),("gowtham",35)]
print(type(list_1))
sorted_list_1=sorted(list_1, key=lambda x:x[1])
print(sorted_list_1)







