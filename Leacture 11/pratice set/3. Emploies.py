#create a class Employee and add salary and increment Properties in it. Write a method salary After incemnet methods with a @ property decoorater with a setter which chamge the vaule of increment based on the salary.

class Employee:
    def __init__(self,salary,incemnet) -> None:
        self.salary = salary
        self.incemnet = incemnet
        
    @property
    def salaryafterincemnet(self):
        return self.salary * (1+self.incemnet)
    
    salaryafterincemnet.setter                  # this is how setter works
    def salaryafterincemnet(self):
        self.salary = self.salary * (1+self.incemnet)
        
        
emp1 = Employee(10000000,0.1)
print(emp1.salaryafterincemnet)