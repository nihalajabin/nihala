class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("name:",self.name,"age:",self.age,"salary:",self.salary)
emplist=[]
i=1
totalage=0
averageage=0
name=[]
j=1
k=0
n=int(input("Enter the number of employees:"))
for i in range(1,n+1):
    nm=input("Enter your name:")
    age=int(input("Enter your age:"))
    sal=int(input("Enter yur salary:"))
    emp=Employee(nm,age,sal)
    emplist.append(emp)
    #print(emp.display())
    if(sal>3000):
        name.append(nm)
        j=j+1
        totalage=totalage+age
p=j-1
averageage=totalage/p
print(j-1,"number of employees have salary greater than 3000")
for k in range(0,p):
    print(name[k])
print("The average age of employees with salary greater then 3000")
print(averageage)
        
    
