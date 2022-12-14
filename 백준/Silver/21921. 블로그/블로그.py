import sys

n, x = map(int,sys.stdin.readline().rstrip().split())
visitor = list(map(int,sys.stdin.readline().rstrip().split()))
if max(visitor) == 0:
    print('SAD')
else:
    max_visitor = sum(visitor[0:x])
    count = 1
    tmp = max_visitor
    for i in range(x, n):
        tmp = tmp - visitor[i-x] + visitor[i]
        if tmp > max_visitor:
            max_visitor = tmp
            count = 1
        elif tmp == max_visitor:
            count += 1
    print(max_visitor, count, sep='\n')