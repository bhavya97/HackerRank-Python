import numpy
i,j = [int(x) for x in input().split()]
array = numpy.array([list(map(int,input().split())) for x in range(i)])
print(max(numpy.min(array,axis=1)))

