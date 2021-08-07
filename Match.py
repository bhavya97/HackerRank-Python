from collections import Counter
F = open('/home/bhavya/Desktop/new', 'r')
data = F.readlines()
bli = []
li2 = []
[bli.append(int(float(data[x].split()[3][0:-1]))) for x in range(0, 101)]
#li2.append(14*5)
#[li2.append(int(data[x].split()[4][0])*5) for x in range(1,101)]
#[print(*x) for x in (zip(li,li2))]
#print(Counter(li))
#print(li2)
#[print(x) for x in enumerate(data,1)]
print(bli)

sli=[]

#[li2.append(int(data[x].split()[8][0:-1])*5) for x in range(101,194)]
[sli.append(int(float(data[x].split()[9][0:-1]))) for x in range(101,194)]
#li2.append(34*5)
sli.append(35883)
#[print(*x) for x in (zip(li,li2))]
print(sli)

F2 = open('/home/bhavya/Desktop/New Text Document.txt','r')
data = F2.readlines()
xli = []
xli2 = []
[xli.append(int(x.split()[2])) for x in data]
[xli2.append(int(x.split()[3])) for x in data]
print(xli)
print(xli2)

print(set(xli).difference(set(bli)))
print(set(bli).difference(set(xli)))
print(set(sli).difference(set(xli2)))
print(set(xli2).difference(set(sli)))