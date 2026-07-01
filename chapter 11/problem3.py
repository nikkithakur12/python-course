class Employee:
    salary = 234
    Increment = 20
     
    @property
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def increment(self,salary):
        self.Increment = ((salary/self.salary)-1)*100
    
e = Employee()
#print(e.salaryAfterincrement)
e.salaryAfterIncrement = 280

    