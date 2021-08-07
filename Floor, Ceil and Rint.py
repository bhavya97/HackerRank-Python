import numpy
A = list(map(float,input().split()))
numpy.set_printoptions(legacy='1.13')
print("{}\n{}\n{}".format(numpy.floor(A),numpy.ceil(A),numpy.rint(A)))
