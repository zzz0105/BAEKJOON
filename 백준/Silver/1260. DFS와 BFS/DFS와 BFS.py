from collections import deque
def dfs(p):
    visited_dfs[p] = 1
    answer_dfs.append(p)
    for i in sorted(graph[p]):
        if not visited_dfs[i]:
            dfs(i)
    return answer_dfs

def bfs(p):
    points = deque()
    points.append(p)
    while points:
        p = points.popleft()
        if not visited_bfs[p]:
            visited_bfs[p] = 1
            points.extend(sorted(graph[p]))
            answer_bfs.append(p)
    return answer_bfs

n, m, v = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []
visited_dfs = [0] * (n+1)
answer_dfs = []
visited_bfs = [0] * (n+1)
answer_bfs = []
for _ in range(m):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

print(*dfs(v), sep=' ')
print(*bfs(v), sep=' ')