t = int(input())
li = [int(input()) for i in range(t)]

height = 1
for i in li:
    for j in range(1,i+1):
        if j % 2 == 1:
            height = height *2
        else:
            height = height +1
    print(height)
    height = 1


