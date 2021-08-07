string = input()
i = 0
L =[]
while i < len(string):
    j=i
    while j <len(string):
        if(string[i] != string[j]):
            break
        j+=1
    L.append((j-i,int(string[i])))
    i=j
print(*L)

from itertools import groupby
print(*[(len(list(k)),int(c)) for c,k in groupby(input())])