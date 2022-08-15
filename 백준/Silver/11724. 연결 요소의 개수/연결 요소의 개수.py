from collections import deque

def bfs(p):
    points = deque()
    points.append(p)
    while points:
        p = points.popleft()
        if not visited[p]:
            visited[p] = 1
            points.extend(graph[p])

n, m = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
visited = [0] * (n+1)
cnt = 0
for j in range(1,n+1):
    if not visited[j]:
        cnt += 1
        bfs(j)

print(cnt)