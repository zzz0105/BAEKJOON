from collections import deque

def bfs(x,y):
    global visited, graph
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    area = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
            nx = x+dx
            ny = y+dy
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]==False:
                visited[nx][ny] = 1
                area += 1
                q.append((nx,ny))
    return area

m, n, k = map(int,input().split())
graph = [[False]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
areas = []
for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x] = True

for i in range(m):
    for j in range(n):
        if graph[i][j]==False and not visited[i][j]:
            areas.append(bfs(i,j))
    
print(len(areas))
print(*sorted(areas), sep=' ')