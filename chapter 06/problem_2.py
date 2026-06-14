marks1 = int(input("Enter the Marks1:" ))
marks2 = int(input("Enter the Marks2:" ))
marks3 = int(input("Enter the Marks3:" ))

# check for total precentage
total_precentage = (100*(marks1+marks2+marks3))/300
if (total_precentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("you are passed",total_precentage)
    
else:
    print("you are failed,try again later", total_precentage)    
    
