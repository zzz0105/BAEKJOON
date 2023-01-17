from collections import deque

def seek(n):
    n_p = deque([n])   # 수빈이 위치
    d = 100000         # 위치의 최대값
    visited = [-1]*(d+1)
    visited[n] = 0
    path = deque()     # 방문 경로
    while n_p:
        x = n_p.popleft()   # 현재 수빈이 위치, 시간
        if x==k:
            while x!=n:
                path.appendleft(x)
                x = visited[x]
            path.appendleft(n)
            return path   
        for nx in [x-1, x+1, 2*x]:
            if 0<=nx<d+1 and visited[nx] == -1:
                visited[nx] = x
                n_p.append(nx)

n, k = map(int, input().split())    #수빈, 동생
answer = seek(n)
print(len(answer)-1)
print(*answer)