class Employee:
    def __init__ (self):
        print("constructer of Employee")
    a = 1
class programmer(Employee):
    def __init__ (self):
        print("constructer of programmer")
    b = 2

class manager(programmer):
    def __init__ (self):
        super().__init__()
        print("constructer of manager")
    c = 3
    
# o = Employee()
# print(o.a)# prints the a attribute


# o = programmer()
# print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)