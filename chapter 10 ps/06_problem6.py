from random import randint

class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
      
    def book (nikki ,fro ,to):
        print(f"train is booked in trainNo:{nikki.trainNo} from {fro} to {to}")
        
    def getstatus(self):
        print(f"trainNo:{self.trainNo}is running on time")
        
    def getfare(self,  fro, to):
        print(f"ticket fare in trainNo:{self.trainNo} from{fro} to {to}is {randint(222,5555)}")
        
        
t = Train(12399)
t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur","Delhi")