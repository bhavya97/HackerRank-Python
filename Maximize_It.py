from itertools import product
k,m = map(int,input().split())
li = []
[li.append(list(map(int,input().split()))[1:]) for _ in range(k)]
print(max(map(lambda x: sum(i*i for i in x),product(*li))))