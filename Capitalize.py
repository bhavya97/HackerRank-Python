str = input()
for x in str.split():
    str = str.replace(x,x.capitalize())
print(str)

