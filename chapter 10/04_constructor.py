class Employee:
  
    language = "python" # This is a class attribute
    salary = 1200000
    
    def __init__(self, name,salary,language): # dunder method which is automaticlly
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    def getinfo():
        print(f"The language is{self.language}.The salary is the {self.salary}")
    @staticmethod    
    def greet():
        print("Good Morning")
        
       
    
nikki = Employee("nikki",130000,"JavaScript")
#nikk.name = "Nikki"
print(nikki.name,nikki.salary,nikki.language)

#harry = Employee()



