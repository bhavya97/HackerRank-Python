x = int(input())
col = (input().split()).index("MARKS")
L = []
[L.append(int(input().split()[col])) for i in range(x)]
print( "{:.2f}".format(sum(L)/x))