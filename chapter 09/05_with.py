f = open("file.txt")
print(f.read())
f.close()

#The same can be written using with statement like this:

with open("file.text") as f:
    f.read()

# you dont have to explicitly close the file

