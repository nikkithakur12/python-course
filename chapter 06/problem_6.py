marks = int(input("Enter your marks:"))
if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90and marks>=80):
    grade = "A"
elif(marks<80and marks>=70):
    grade = "B"
elif(marks<70and marks>=60):
    grade = "C"
elif(marks<60and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"
print("Your grade is:",grade)