import heapq, sys

def dijkstra(start):
    global V, graph, distance
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]:
            continue
        for to, d in graph[now]:
            tmp = dist + d
            if distance[to] > tmp:
                distance[to] = tmp
                heapq.heappush(hq, (tmp, to))
            
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))
distance = [float('inf')]*(V+1)
dijkstra(K)
for i in range(1,V+1):
    print('INF' if distance[i]==float('inf') else distance[i])