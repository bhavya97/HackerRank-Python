from collections import OrderedDict
d = OrderedDict()
for x in range(int(input())):
    s = input()
    val = s.split()[-1]
    k = s[0:len(s)-len(val)-1]
    d[k] = d[k] + int(val) if k in d.keys() else int(val)
[print(x,y) for x,y in d.items()]

