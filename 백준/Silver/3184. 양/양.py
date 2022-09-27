import sys
from collections import deque

def bfs(x,y):
    pos = deque()
    pos.append((x,y))
    if yard[x][y]=='o':
        sheep, wolf = 1, 0
    if yard[x][y] == 'v':
        sheep, wolf = 0, 1
    visited[x][y] = True
    while pos:
        x, y = pos.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<r and 0<=ny<c and visited[nx][ny]==False and yard[nx][ny]!='#':
                visited[nx][ny] = True
                if yard[nx][ny]=='o':
                    sheep += 1
                if yard[nx][ny] == 'v':
                    wolf += 1
                pos.append((nx,ny))
    if wolf >= sheep:
        sheep -= wolf
        if sheep < 0:
            sheep = 0
    else:
        wolf = 0
    return (sheep, wolf)

r, c = map(int,sys.stdin.readline().rstrip().split())
yard = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[False]*c for _ in range(r)]
sw = [0, 0]
for i in range(r):
    for j in range(c):
        if (yard[i][j]=='v' or yard[i][j]=='o') and visited[i][j]==False:
            tmp = bfs(i,j)
            sw[0] += tmp[0]
            sw[1] += tmp[1]
print(sw[0], sw[1])