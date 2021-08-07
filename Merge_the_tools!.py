S,K = input(),int(input())
for i in range(0,(len(S)),K):
    temp = S[i:i+K]
    L = []
    [L.append(x) for x in temp if x not in L]
    print(''.join(L))