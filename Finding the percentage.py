marks = {}
for x in range(0,int(input())):
    line = input().split()
    marks[line[0]] = list(map(float,line[1:]))
print(sum(marks[input()])/3)
