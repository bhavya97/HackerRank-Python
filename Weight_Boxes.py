n = [int(i) for i in input().split()]
max = max(n)
n.remove(max)
print(sum(n))
