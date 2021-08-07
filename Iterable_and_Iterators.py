from itertools import combinations

N = int(input()); a = input().split(); K = int(input())
c = list(combinations(a,K))
result = [1 for i in range(len(c)) if 'a' in c[i]]
print(sum(result)/len(c))

'''
from math import factorial 
def C(n, k):
    if n < k:
        return 0
    return factorial(n) // factorial(n-k)

N = int(input())
n_a = input().split().count('a')
K = int(input())

print('%.3f' % (1 - C(N - n_a, K) / C(N, K)))
'''
