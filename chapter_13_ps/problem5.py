from functools import reduce
l = [239,434,654,867,98,23,456,787]
def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater,l))