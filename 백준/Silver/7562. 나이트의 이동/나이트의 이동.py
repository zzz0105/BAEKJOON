from collections import deque

def bfs(now, end):
    if now == end:
        return 0
    pos = deque()
    pos.append(now)
    visited = [[0]*l for _ in range(l)]
    move = [(2,1),(1,2),(2,-1),(1,-2),(-1,-2),(-2,-1),(-1,2),(-2,1)]
    while pos:
        x, y = pos.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx == end[0] and ny == end[1]:
                return visited[x][y]+1
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                pos.append((nx,ny))

tc = int(input())
for _ in range(tc):
    l = int(input())
    now = list(map(int,input().split()))
    end = list(map(int,input().split()))
    print(bfs(now,end))