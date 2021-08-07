n = int(input())
marksheet = [[str(input()), float(input())] for x in range(n)]
sec_high = sorted(list(set(marks for names, marks in marksheet)))[1]
names = list()
[names.append(x[0]) for x in marksheet if sec_high == x[1]]
for x in sorted(names): print(x)
