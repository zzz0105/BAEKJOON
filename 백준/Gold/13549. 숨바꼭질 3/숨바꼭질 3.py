from collections import deque

n, k = map(int,input().split())
position = [0] * 100001
position[n] = 1
moving = deque()
moving.append(n)
while moving:
    x = moving.popleft()    # 현재 위치
    if x == k:
        print(position[k]-1)
        break
    else:
        for dx in (-1,1):
            nx = x + dx     # 걸어서
            if 0<=nx<=100000 and (position[nx]==0 or position[nx]>position[x]+1):
                position[nx] = position[x] + 1
                moving.append(nx)
        tx = x * 2          # 순간이동
        if 0<=tx<=100000 and (position[tx]==0 or position[tx]>position[x]):
            position[tx] = position[x]
            moving.append(tx)