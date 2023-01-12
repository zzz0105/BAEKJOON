from collections import deque

def calculation(s, e):
    q = deque()
    q.append(s)
    visited = [-1]*(n+1)
    visited[s] = 0
    while q:
        now = q.popleft()
        if now == e:
            return visited[now]
        for next in relations[now]:
            if visited[next]==-1:
                visited[next] = visited[now]+1
                q.append(next)
    return -1

n = int(input())
p1, p2 = map(int,input().split())
m = int(input())
relations = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    relations[x].append(y)
    relations[y].append(x)
print(calculation(p1,p2))