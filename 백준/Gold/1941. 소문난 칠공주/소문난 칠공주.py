from itertools import combinations
from collections import deque

def check_s(arr):
    cnt = 0
    for a in arr:
        if students[a[0]][a[1]]=='S':
            cnt += 1
    return True if cnt>=4 else False

def check_ad(arr):
    visited = [0]*7
    q = deque()
    q.append(arr[0])
    visited[0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
            nx = x+dx
            ny = y+dy
            if 0<=nx<5 and 0<=ny<5 and (nx,ny) in arr:
                idx = arr.index((nx,ny))
                if not visited[idx]:
                    visited[idx] = 1
                    q.append((nx,ny))
    return False if False in visited else True

students = [tuple(input()) for _ in range(5)]
positions = [(i,j) for i in range(5) for j in range(5)]
combis = combinations(positions, 7)
answer = 0
for combi in combis:
    if check_s(combi) and check_ad(combi):
        answer += 1
print(answer)