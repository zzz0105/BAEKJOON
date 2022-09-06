from collections import deque

def bfs(i, j, team):
    pos = deque()
    pos.append((i,j))
    soldiers[i][j] = ' '
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    sd = 1
    while pos:
        i, j = pos.popleft()
        for di, dj in move:
            ni = i + di
            nj = j + dj
            if 0<=ni<m and 0<=nj<n and soldiers[ni][nj]==team:
                sd += 1
                soldiers[ni][nj] = ' '
                pos.append((ni, nj))
    return sd**2

n, m = map(int,input().split())
soldiers = [list(input()) for _ in range(m)]
white = 0
blue = 0
for x in range(m):
    for y in range(n):
        if soldiers[x][y]=='W':
            white += bfs(x,y,'W')
        elif soldiers[x][y]=='B':
            blue += bfs(x,y,'B')
print(white, blue)