n = int(input())
scores = map(int,input().split())
m = int(input())
alice = map(int,input().split())

leaderboad = sorted(set(scores),reverse=True)
l = len(leaderboad)

for i in alice:
    while(l > 0) and i >=leaderboad[l-1]:
        l -= 1
    print(l+1)
