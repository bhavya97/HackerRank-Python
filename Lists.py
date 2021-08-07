l = []
for x in range(0,int(input())):
    s = input().split()
    cmd = s[0]
    if cmd != "print":
        eval("l."+cmd+"("+",".join(s[1:])+")")
    else:
        print(l)
