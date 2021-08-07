li = [int(i) for i in input().split()]
length = [li[ord(i)-ord('a')] for i in input()]
print(max(length)*len(length))

