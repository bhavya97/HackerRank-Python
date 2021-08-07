n_elements = map(int,input().split())
a,b = set(map(int,input().split())),set(map(int,input().split()))
print(a.intersection(n_elements))
print(b.intersection(n_elements))
