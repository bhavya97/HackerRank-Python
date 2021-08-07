import numpy
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det([numpy.array(input().split(),float) for x in range(int(input()))]))