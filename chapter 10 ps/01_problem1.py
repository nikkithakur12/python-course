class programmer:
    company = "Microsoft"
    def __init__(self, name, salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = programmer("Nikki",12000,247452)
print(p.name,p.salary,p.pin,p.company)
r = programmer("Rohan",12000,247452)   
print(r.name,r.salary,r.pin,r.company)