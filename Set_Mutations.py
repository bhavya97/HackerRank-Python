N_a = int(input())
A = set(input().split())
[eval('A.{}({})'.format(input().split()[0],set(input().split()))) for x in range(int(input()))]
print(sum(map(int,A)))