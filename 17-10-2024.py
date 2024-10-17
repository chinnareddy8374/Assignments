# Union: it reyturns both sets.
s12_1={1,2,3,4,5}
s12_2={1,2,6,7,8,9,10}
s12=s12_1.union(s12_2)
print(s12)
#            (or)
s12=s12_1|s12_2
print(s12)

# Intersection : it returns common elements in both sets.
s13_1={1,2,3,4,5}
s13_2={3,4,5,6,7}
s13=s13_1.intersection(s13_2)
print(s13)
#           (or)
s13=s13_1&s13_2
print(s13)

# Difference : it returned set contains items that exist only in the first set, and not in both sets.
s14_1={1,2,3,4,5}
s14_2={3,4,5,6,7}
s14=s14_1.difference(s14_2)
print(s14)
#           (or)
s14=s14_1-s14_2
print(s14)

# symmeteric_difference : it returns a set that contains all items from both set, but not the items that are present in both sets.
s15_1={"apple", "banana", "cherry"}
s15_2={"google", "microsoft", "apple"}
s15=s15_1.symmetric_difference(s15_2)
print(s15)
#               (or)
s15=s15_1^s15_2
print(s15)

# Write a python program to iterate over set
s16=set([0,1,2,3,4,5,6])
print(s16)
for i in s16:
    print(i,end=' ')
print('------------------------------------------------')

# Write a python program to add member(s) to a set.
s17={"apple","banana","cherry","lemon","apricot","plum"}
s17.add("papaya")
print(s17)

# Write a program to remove items from a given set.
s18={"apple","banana","cherry","lemon","apricot","plum","papaya"}
s18.remove("papaya")
print(s18)

# Write a python program to remove an iteam from a set if it is present in the set.
s19={"apple","banana","cherry","lemon","apricot","plum"}
if "lemon" in s19:
    print("yes, it exist")
    s19.remove("lemon") 
print(s19)

# Write a python program to create an interaction of sets.
s20_1={"apple", "banana", "cherry"}
s20_2={"google", "microsoft", "apple"}
s20=s20_1&s20_2
print(s20)

# Write a python program to create a union of set.
s21_1={"apple", "banana", "cherry"}
s21_2={"google", "microsoft", "apple"}
s21=s21_1|s21_2
print(s21)

# Write a program to remove all elements from given set.
s22={"apple", "banana", "cherry","google", "microsoft", "apple"}
print(s22)
s22.clear()
print(s22)