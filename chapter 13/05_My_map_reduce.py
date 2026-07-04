from functools import reduce
# Map Example

l = [1,2,3,4,5,6]
square = lambda X : X*X
sqLst = map(square,l)
print(list(sqLst))
# Filter Example

def even(a):
    if (a%2==0):
        return True
    return False
OnlyEven = filter(even,l)
print(list(OnlyEven))

# Reduce Example
def sum (a,b):
    return a + b
multiply = lambda x,y:x*y
print(reduce(sum,l))
print(reduce(multiply,l))