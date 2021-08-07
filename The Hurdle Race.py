n,k = map(int,input().split())
li = [int(i) for i in input().split()]
print(max(0,max(li)-k))

'''max = 0
for i in li:
    if max < i and i > k:
        max = i
print(max-k) if max > k else print(0)
'''