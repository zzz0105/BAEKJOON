import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(V):
    global count
    visited[V] = count
    graph[V].sort()
    for con in graph[V]:
        if visited[con] == 0:
            count += 1
            dfs(con)

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
count = 1
dfs(R)
print(*visited[1:], sep='\n')