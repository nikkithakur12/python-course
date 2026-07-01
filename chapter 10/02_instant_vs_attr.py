class Employee:
  
    language = "python" # This is a class attribute
    salary = 1200000
    
harry = Employee()

harry.language = "JavaScript" #This is an instance/object attribute
print(harry.language,harry.salary)

