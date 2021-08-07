import numpy
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)
print("{}\n{}".format(numpy.inner(A,B),numpy.outer(A,B)))

'''
import numpy

A, B = [numpy.array(raw_input().split(), int) for _ in range(2)]
print '\n'.join(str(op(A, B)) for op in (numpy.inner, numpy.outer))
'''