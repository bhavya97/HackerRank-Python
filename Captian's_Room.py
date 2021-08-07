from collections import Counter
input()
print(Counter(input().split()).most_common()[-1][0])

'''
k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-( sum(arr)))//(k-1))
'''
