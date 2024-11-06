#nested class:- it is nothing but a class in a class
 
#example:-
class employee:
    def __init__(self,name,age,skillset):
        self.name = name
        self.age = age
        self.skillset = skillset
   
    def display(self):
        print(self.name)
        print(self.age)
        print(self.skillset)
   
    class employement:
        def __init__(self,cmpnyname,salary,domain):
            self.cmpnyname = cmpnyname
            self.salary = salary
            self.domain = domain
        def display(self):
            print(self.cmpnyname)
            print(self.salary)
            print(self.domain)
   
    m = employement("skywaves",25000,"python")
    m.display()
 
p = employee("reddy",28,"pyton,django,mySQL")
p.display()

