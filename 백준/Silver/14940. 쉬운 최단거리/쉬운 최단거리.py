from collections import deque

def bfs(arr, goal):
    global n, m, visited
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append(goal)
    visited[goal[0]][goal[1]] = 1
    arr[goal[0]][goal[1]] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                arr[nx][ny] = arr[x][y] + 1

n, m = map(int,input().split())
arr = []
goal = (-1,-1)
for i in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
    if goal == (-1,-1):
        if 2 in tmp:
            goal = (i, tmp.index(2))
bfs(arr, goal)
for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and arr[i][j]==1:
            print(-1, end =' ')
        else:
            print(arr[i][j], end =' ')
    print()