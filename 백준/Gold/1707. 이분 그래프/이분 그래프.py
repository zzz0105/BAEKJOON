from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    global visited
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = -1 * visited[x]
                # 연결된 노드와 다른 색으로 칠한다
            elif visited[nx] == visited[x]:
            # 같은 색의 노드가 연결되어있는지 확인
                return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,V+1):
        if not visited[i]:
            flag = bfs(i)
            if not flag:
                break
    print('YES' if flag else 'NO')    