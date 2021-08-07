from itertools import combinations
string,k = input().split()
string = sorted(string)
[print( *[''.join(x) for x in combinations(string,int(i))],sep="\n") for i in range(1,int(k)+1)]
