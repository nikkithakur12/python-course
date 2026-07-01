class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
# class programmer:
#     company = "ITC Infotech" 
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
        
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with{self.Langoage}")
        
class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
       print(f"The name is {self.name} and he is good with{self.Langoage}")
    
a = Employee()
b = programmer()
print(b.company,a.company)
        
            
