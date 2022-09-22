from collections import deque

def bfs(x, y):
    global arr
    land = deque()
    land.append((x,y))
    while land:
        x, y = land.popleft()
        for dx, dy in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<h+2 and 0<=ny<w+2 and arr[nx][ny]=='1':
                land.append((nx,ny))
                arr[nx][ny] = '0'
    return 1

while True:
    w, h = map(int,input().split())
    island = 0
    if w == 0 and h == 0:
        break
    arr = [['0']*(w+2)] + [['0']+list(input().split())+['0'] for _ in range(h)] + [['0']*(w+2)]
    for i in range(h+2):
        for j in range(w+2):
            if arr[i][j] == '1':
                island += bfs(i,j)
    print(island)