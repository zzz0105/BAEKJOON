from collections import deque

def bfs(j, i, cnt):
    baechu = deque()
    baechu.append((j, i))
    while baechu:
        j, i = baechu.popleft()
        for di, dj in move:
            ni = i + di
            nj = j + dj
            if 0<=ni<m and 0<=nj<n and farm[nj][ni]==1:
                farm[nj][ni] = 0
                baechu.append((nj,ni))
    return cnt+1

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    farm = [[0]*m for _ in range(n)]
    cnt = 0
    move = [(0,1), (1,0), (0,-1), (-1,0)]
    for _ in range(k):
        x, y = map(int,input().split())
        farm[y][x] = 1
    for j in range(n):
        for i in range(m):
            if farm[j][i] == 1:
                cnt = bfs(j, i, cnt)
    print(cnt)