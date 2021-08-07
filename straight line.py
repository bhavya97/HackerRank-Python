n = int(input())
li = [int(i) for i in input().split()]
points = []
for i in range(0,n*2,2):
    points.append([li[i],li[i+1]])
x0,y0  = points[0]
points = [ (x,y) for x,y in points if x != x0 or y != y0 ]      # Other points
slopes = [ (y-y0)/(x-x0) if x!=x0 else None for x,y in points ] # None for vertical Line
res = all( s == slopes[0] for s in slopes)

if(res == True):
    print("1x-1y=0")
else:
    print(0)