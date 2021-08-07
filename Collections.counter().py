from collections import Counter
x = int(input())
L = Counter(map(int,input().split()))
income = 0
for x in range(int(input())):
    size,price = map(int,input().split())
    if (L[size]):
        L[size] -=1
        income += price
print(income)
