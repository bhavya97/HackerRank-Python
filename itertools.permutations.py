from itertools import permutations
string,k = input().split()
print(*[''.join(x) for x in permutations(sorted(string),int(k))],sep="\n")
