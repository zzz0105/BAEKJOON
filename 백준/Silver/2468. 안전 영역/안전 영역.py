from collections import deque

def dfs(x, y, h):
    global heights
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and heights[nx][ny] > h and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return 1

n = int(input())
heights = []
cnts = []
max_height = 0
for _ in range(n):
    heights.append(list(map(int,input().split())))
    max_height = max(max_height, max(heights[-1]))
for rain in range(1+max_height):
    area = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if rain < heights[i][j] and visited[i][j]==0:
                area += dfs(i, j, rain)
    if area == 0:
        break
    cnts.append(area)
    rain += 1
print(max(cnts))