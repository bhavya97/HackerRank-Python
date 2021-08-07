from itertools import product
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
print( [(x,y) for x in A for y in B].__class__ )
print(*list(product(A,B)),sep=" ")

