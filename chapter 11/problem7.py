class vector:
    def __init__(self,l):
        self.l = l
        
    def __len__(self):
         return len (self.l)
     
# test the implementation

v1 = ([1 , 2 , 3])
print(len(v1))