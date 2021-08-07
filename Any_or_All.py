n,m = int(input()),input().split()
print(all(int(x) > 0 for x in m) and any(y==y[::-1] for y in m))