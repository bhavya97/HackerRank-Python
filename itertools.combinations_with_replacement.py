from itertools import combinations_with_replacement
string,k = input().split()
print( *[''.join(x) for x in combinations_with_replacement(sorted(string),int(k))],sep="\n")

