from collections import deque

def bfs(x, y):
    position = deque()
    position.append((x, y))
    while position:
        x, y = position.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y] + 1
                position.append((nx, ny))
    return maze[n-1][m-1]

n, m = map(int,input().split())
maze = [list(map(int,list(input()))) for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
print(bfs(0,0))