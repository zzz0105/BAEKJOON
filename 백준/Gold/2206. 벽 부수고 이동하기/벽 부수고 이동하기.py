from collections import deque
import sys

def bfs(x, y, wall_break):
    global arr, visited, n, m
    move = [(-1,0),(0,1),(1,0),(0,-1)]
    q = deque()
    q.append((x, y, wall_break))
    visited[x][y][wall_break] = 1
    while q:
        x, y, wall_break = q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][wall_break]
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m:
                if wall_break == 0 and arr[nx][ny] == 1:
                    visited[nx][ny][wall_break+1] = visited[x][y][wall_break] + 1
                    q.append((nx,ny, wall_break+1))
                elif arr[nx][ny] == 0 and visited[nx][ny][wall_break]==0:
                    visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                    q.append((nx,ny,wall_break))
    return -1

n, m = map(int,sys.stdin.readline().rstrip().split())
arr = [tuple(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(bfs(0, 0, 0))