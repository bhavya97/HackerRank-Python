x = int(input())
dict = {}
for _ in range(x):
    str = input()
    if str in dict:
        dict[str] = dict[str] +1
    else:
        dict[str] = 1
print(dict.__len__())
print(*dict.values())

