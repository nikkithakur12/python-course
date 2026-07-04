def divisible5(n):
    if (n%5==0):
        return True
    return False
a = [34,65,754,645,4344,232,456,867]
f = list(filter(divisible5,a))
print(f)


