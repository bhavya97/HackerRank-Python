str = input()
stuart_sc = 0
kevin_sc = 0
vowels = "AEIOU"
for x in range (len(str)):
    if str[x] in (vowels):
        kevin_sc += (len(str)-x)
    else:
        stuart_sc +=(len(str)-x)

if kevin_sc < stuart_sc:
    print("Stuart",stuart_sc)
elif kevin_sc > stuart_sc:
    print("Kevin",kevin_sc)
else:
    print("Draw")
