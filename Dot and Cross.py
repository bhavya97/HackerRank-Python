import numpy
n = int(input())
print(numpy.dot([list(map(int,input().split())) for x in range(n)],[list(map(int,input().split())) for x in range(n)]))
