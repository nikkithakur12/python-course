class twodvactor:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def show(self):
      print(f"the vactor is {self.i}i + {self.j}j")
        
class threedvactor(twodvactor):
    def __init__(self,i , j , k):
        super().__init__(i , j)
        self.k = k
        
        
    def show(self):
      print(f"The vactor is {self.i}i + {self.k}j + {self.j}k ")
        
        
a = twodvactor(5,6)
a.show()
b = threedvactor(5,7,6)
b.show()