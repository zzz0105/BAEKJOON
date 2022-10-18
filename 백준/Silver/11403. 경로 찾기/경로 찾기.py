n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if g[a][b] or (g[a][k] and g[k][b]):
                g[a][b] = 1

for row in g:
    print(*row, sep=' ')