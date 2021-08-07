int(input())
set = set(map(int,input().split()))
for _ in range(int(input())):
    eval('set.{0}({1})'.format(*input().split()+['']))
print(sum(set))
