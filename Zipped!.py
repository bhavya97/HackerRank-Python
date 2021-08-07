x,y = [int(n) for n in input().split()]
array = [[float(m) for m in input().split()] for _ in range(y)]
print(*[sum(i)/y for i in zip(*array)],sep="\n")
