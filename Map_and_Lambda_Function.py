cube = lambda x: (pow(x,3))

def fibonacci(n):
    li = [0,1]
    [li.append(li[x-1]+li[x]) for x in range(1,n-1)]
    return li[0:n]

print(fibonacci(int(input())))
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


'''
cube = lambda x: x**3

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

print(list(map(cube, list(fibonacci(int(input()))))))
'''