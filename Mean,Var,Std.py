import numpy
i,j = [int(x) for x in input().split()]
array = numpy.array([list(map(int,input().split())) for x in range(i)])
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(array,axis=1))
print(numpy.var(array,axis=0))
print(numpy.std(array,axis=None))


'''
n = np.array([input().split() for _ in range(int(input().split()[0]))],int)
print(np.mean(n,axis=1),np.var(n,axis=0),np.std(n),sep="\n")
'''