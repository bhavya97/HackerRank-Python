A = set(input().split())
check = True
for x in range(int(input())):
    if not A.issuperset(set(input().split())):
        check = False
        break
print("True") if check else print("False")


'''
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))

'''