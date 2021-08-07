from collections import deque
d = deque()
for _ in range(int(input())):
    str =input().split()
    print("d.{}({})".format(*str,""))
    eval("d.{}({})".format(*str,""))
print(*d)