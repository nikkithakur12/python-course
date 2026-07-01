class Employee:
  
    language = "py" # This is a class attribute
    salary = 1200000
    
harry = Employee()
harry.name = "Harry" #This is an instance/object attribute
print(harry.name,harry.language,harry.salary)

nikki = Employee()
nikki.name = "nikki thakur"
print(nikki.name,nikki.salary ,nikki.language)

#  Here name is instance attribute and salary and language are class attribute as they directly
# belong to the class