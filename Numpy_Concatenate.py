import numpy
N,M,P = map(int,input().split())
arrayA = numpy.array([list(map(int,input().split())) for x in range(N)]) #both results the same
arrayB = numpy.array([input().split() for y in range(M)],int)
print(numpy.concatenate((arrayA,arrayB)))
