import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
bus = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    start, end, price = map(int,sys.stdin.readline().rstrip().split())
    bus[start-1][end-1] = min(price, bus[start-1][end-1])

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                bus[a][b] = 0
            else:
                bus[a][b] = min(bus[a][b], bus[a][k]+bus[k][b])

for r in bus:
    for c in r:
        if c == float('inf'):
            print(0, end=' ')
        else:
            print(c, end=' ')
    print()