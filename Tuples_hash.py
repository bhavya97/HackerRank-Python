input()
list = tuple(map(int,(input().split())))
print(list.__hash__())