a = int(input("Enter your age: "))

# if statement no:1
if(a%2==0):
    print("a is even ")
    
#end of if statement no:2
    
#if statement no:2
if(a>18):
    print("you are above the age of consent")
    print("good for you")
# end of if statement no:2  
# if statement no:3
if(a==28):
    print("you are equal  the age of the consent")  
# end of the statement no:3    
elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("you are blow the age of consent")
    
print("end of the programm")
    