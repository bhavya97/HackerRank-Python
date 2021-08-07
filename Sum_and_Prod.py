import numpy
N,M = map(int,input().split())
print(numpy.prod(numpy.sum(numpy.array([input().split() for x in range(N)],dtype=int),axis=1)))
#print(numpy.prod(numpy.sum([list(map(int, input().split())) for _ in range(N)],axis=0)))
