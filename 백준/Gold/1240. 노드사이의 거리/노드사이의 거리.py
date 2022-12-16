from collections import deque

def bfs(n1, n2):
    global graph, N
    q = deque()
    q.append((n1, 0))
    visited = [0]*(N+1)
    while q:
        n, d = q.popleft()
        if n == n2:
            return d
        for con, con_d in graph[n]:
            if not visited[con]:
                visited[con] = True
                q.append((con, d+con_d))

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, d = map(int,input().split())
    graph[u].append((v,d))
    graph[v].append((u,d))
for _ in range(M):
    n1, n2 = map(int,input().split())
    print(bfs(n1, n2) if n1!=n2 else 0)