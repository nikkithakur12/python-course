class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
        
class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of  all. the languages is your language:{self.language}")
        
class programmer(Employee,coder):
    company = "ITC Infotech"
    def showLanguage(self):
       print(f"The name is {self.company} and he is good with {self.language}language")
    
a = Employee()
b = programmer()
b.show()
b.printlanguages()
b.showLanguage()
        