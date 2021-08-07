i,j,k = map(int,input().split())
count = 0
for _ in range(i,j+1,1):
    if (_ - int(str(_)[::-1])) % k == 0:
        count+=1
print(count)