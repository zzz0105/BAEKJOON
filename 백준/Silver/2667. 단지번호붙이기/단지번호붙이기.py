from collections import deque

def bfs(x, y, complex):
    apt = deque()
    apt.append((x, y))
    arr[x][y] = 0
    cnt = 1
    while apt:
        x, y = apt.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                cnt += 1
                arr[nx][ny] = 0
                apt.append((nx, ny))
    complex_cnt[complex] = cnt

n = int(input())
arr = [list(map(int,list(input()))) for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
complex = 0
complex_cnt = {}
for x in range(n):
    for y in range(n):
        if arr[x][y]==1:
            complex += 1
            bfs(x, y, complex)

answer = complex_cnt.values()
print(len(answer), *sorted(answer), sep='\n')