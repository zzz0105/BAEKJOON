from collections import deque

def bfs(ripe_pos):
    global tomato, tomato_status, day
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    tomato_pos = deque()
    tomato_pos.extend(ripe_pos)
    while tomato_pos:
        x, y, day = tomato_pos.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy 
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                tomato[nx][ny] = 1
                tomato_pos.append((nx,ny, day+1))
                tomato_status[0]-=1
                tomato_status[1]+=1

m, n = map(int,input().split())
tomato = []
tomato_status = {-1:0, 0:0, 1:0 }
ripe_pos = []
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        tomato_status[tmp[j]] += 1
        if tmp[j] == 1:
            ripe_pos.append((i,j,0))
    tomato.append(tmp)
if tomato_status[0] == 0:
    print(0)
else:
    bfs(ripe_pos)
    print(-1 if tomato_status[0] else day)