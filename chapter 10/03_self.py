class Employee:
  
    language = "python" # This is a class attribute
    salary = 1200000
    def getinfo(self):
        print(f"The language is{self.language}.The salary is the {self.salary}")
    @staticmethod    
    def greet():
        print("Good Morning")
    
harry = Employee()

#harry.language = "JavaScript" #This is an instance/object attribute
harry.getinfo()
harry.greet()
#Employee.getinfo(harry)
