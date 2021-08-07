n = int(input())
count = 0
while(n!=0):
    count = count +1
    if n%2 == 0:
        n = n/2
    else:
        n = n-1
print(count)