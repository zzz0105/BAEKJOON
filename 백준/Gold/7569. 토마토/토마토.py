import sys
from collections import deque

def bfs(ripe_pos):
    global tomato, tomato_status, day
    move = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]
    tomato_pos = deque()
    tomato_pos.extend(ripe_pos)
    while tomato_pos:
        h, x, y, day = tomato_pos.popleft()
        for dh, dx, dy in move:
            nh = h + dh
            nx = x + dx
            ny = y + dy 
            if 0<=nh<H and 0<=nx<N and 0<=ny<M and tomato[nh][nx][ny]==0:
                tomato[nh][nx][ny] = 1
                tomato_pos.append((nh, nx, ny, day+1))
                tomato_status[0]-=1
                tomato_status[1]+=1

M, N, H = map(int,sys.stdin.readline().rstrip().split())
tomato = []
tomato_status = {-1:0, 0:0, 1:0 }
ripe_pos = []
for i in range(H):
    tomato_tmp = []
    for j in range(N):
        tmp = list(map(int,sys.stdin.readline().rstrip().split()))
        for k in range(M):
            tomato_status[tmp[k]] += 1
            if tmp[k] == 1:
                ripe_pos.append((i,j,k,0))
        tomato_tmp.append(tmp)
    tomato.append(tomato_tmp)

if tomato_status[0] == 0:
    print(0)
else:
    bfs(ripe_pos)
    print(-1 if tomato_status[0] else day)