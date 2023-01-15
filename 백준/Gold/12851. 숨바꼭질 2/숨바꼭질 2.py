from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    time = [-1]*100001
    time[x] = 0
    method = [0]*100001
    method[x] = 1
    while q:
        x = q.popleft()
        for dx in (1, -1, x):
            nx = x + dx
            if 0<=nx<100001:
                if time[nx]==-1:
                    time[nx] = time[x]+1
                    method[nx] = method[x]
                    q.append(nx)
                elif time[nx]==time[x]+1:
                    method[nx] += method[x]
    return (time[K], method[K])

N, K = map(int,input().split())
print(*bfs(N), sep='\n')