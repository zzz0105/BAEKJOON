from collections import deque

def solution(n, edge):
    def bfs(i):
        q = deque([i])
        visited = [-1]*(n+1)
        visited[i] = 0
        dist_dict = {0:[i]}
        while q:
            now = q.popleft()
            for cn in graph[now]:
                if visited[cn]==-1:
                    visited[cn]=visited[now]+1
                    q.append(cn)
                    dist_dict[visited[cn]]=dist_dict.get(visited[cn],[])+[cn]
        return len(dist_dict[max(dist_dict)])
    
    graph = [[] for _ in range(n+1)]
    for v1,v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return bfs(1)