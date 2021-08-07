from collections import deque
d = deque()

def check(deq):
    while len(deq) != 1:
        if deq[0] > deq[-1]:
            left = deq[0]
            if left >= deq[1]:
                deq.popleft()
            else:
                return "No"
        else:
            right = deq[-1]
            if right >= deq[-2]:
                deq.pop()
            else:
                return "No"
    return "Yes"

for _ in range(int(input())):
    input()
    d.extend(map(int, input().split()))
    print(check(d))
    d.clear()

'''
for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print "Yes" if i == l - 1 else "No"
'''