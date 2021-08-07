l,p = 0,5
for i in range(int(input())):
    l += int(p/2)
    p = int(p/2)*3
print(l)