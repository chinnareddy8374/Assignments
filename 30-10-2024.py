# classmethod:- The classmethod decorator in Python is used to defi ne a class method.
# decorator :- Decorators in Python are a way to modify or enhance the behavior of functions or classes without directly modifying their source code.
# static variable :- When we declare a variable inside a class but outside method is called static variable.

class Employee:
    company="skywaves softwares"
    def getdetails(self):
        self.ename=input("enter employee name : ")
        self.eid = int(input("enter employee id : "))
        self.esalary = int(input("enter employee salary : "))
        self.desig = input("enter employee designation : ")

    def empdetails(self):
        print("Employee name : ", self.ename)
        print("Employee id : ", self.eid)
        print("Employee Salary : ", self.esalary)
        print("Employee designation : ", self.desig)
e1 = Employee()
print(e1)
e1.getdetails()
e1.empdetails()

e2 = Employee()
print(e2)
e2.getdetails()   
e2.empdetails()



# Write a program to  get student details?
class college:
    college_name= "Narayana engineering college"
    def __init__(self,):
        self.sname = input("Enter the student name here : ")
        self.sid = int(input("Enter the student roll no here : "))
        self.sbranch = input("Enter the branch here : ")
        self.saddress =str(input("Enter a address here : "))

    def studentdetails(self):
        print("Student Name : ", self.sname)
        print("Student id : ", self.sid)
        print("Student Branch : ", self.sbranch)
        print("Student Address : ", self.saddress)

s1=college()
print(s1)
s1.studentdetails()

#                           (OR)

class college:
    college_name= "Narayana engineering college"
    def __init__(self,sname,sid,sbranch,saddress):
        self.sname = sname
        self.sid = sid
        self.sbranch = sbranch
        self.saddress = saddress

    def studentdetails(self):
        print(self.sname)
        print(self.sid)
        print(self.sbranch)
        print(self.saddress)

s1=college("hari",10002,"EEE","Hyderabad")
s1.studentdetails()

# Write a program to deposit or withdraw money in a bank account?
class account:
    def __init__(self):
        self.balance = 0
        print("New Account Created.")
    def deposit(self):
        amount = float(input("Enter amount to Deposit : "))
        self.balance += amount
        print("New Balance : ", self.balance)
    def withdraw(self):
        amount = float(input("Enter amount to Withdraw : "))
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            print("New Balance : ", self.balance)
    def Total_Balance(self):
        print("Total Balance : ", self.balance)

account = account()
account.deposit()
account.withdraw()
account.Total_Balance()
