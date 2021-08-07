for i in range(int(input())):
    n,k = map(int,input().split())
    disciplined = 0
    for j in input().split():
        if int(j) <= 0:
            disciplined = disciplined +1
    if k <= disciplined:
        print("NO")
    else:
        print("YES")



