from collections import deque

def bfs(x, y):
    area = 1
    p = deque()
    p.append((x, y))
    visited[x][y] = 1
    while p:
        x, y = p.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and pic[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny] =  1
                area += 1
                p.append((nx,ny))
    return area

n, m = map(int,input().split())
pic = []
is_empty = True
for i in range(n):
    pic += [list(map(int, input().split()))]
    if 1 in pic[i]:
        is_empty = False
visited = [[0] * m for _ in range(n)]
move = [(1,0), (0,1), (-1,0), (0,-1)]
max_area = 0
cnt = 0
if not is_empty:
    for x in range(n):
        for y in range(m):
            if pic[x][y]==1 and visited[x][y]==0:
                max_area = max(bfs(x, y), max_area)
                cnt += 1
print(cnt)
print(max_area)