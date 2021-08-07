for x in range(int(input())):
    input()
    a = set(input().split())
    input()
    b = set(input().split())
    if a.issubset(b): print("True")
    else: print("False")
