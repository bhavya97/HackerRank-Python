'''
xk = input().split()
x = int(xk[0])          #python eval()
print(eval(input()) == int(xk[1]))
'''

'''
x = input() #python evaluation hackerrank
exec(x)
'''

str = "Bhavya Bhatia"
print(list(str.split()[1]))

n,m = map(int,input().split())
rows = [input() for _ in range(n)]
k = int(input())

for row in sorted(rows ,key =lambda row: int(row.split()[k])):
    print(row)
