# Using walrus operator
if (n := len([0,4,45,5,6,6,4,]))>3:
    print(f"list is to long({n}element, expected >=3)")
#output:list is to long(7element, expected >=3)