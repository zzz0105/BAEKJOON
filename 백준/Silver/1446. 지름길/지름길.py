import heapq, sys

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in highway[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n, d = map(int, sys.stdin.readline().rstrip().split())
highway = [[] for _ in range(d+1)]
distance = [float('inf')] * (d+1)
for i in range(d):
    highway[i].append((i+1, 1))
for _ in range(n):
    start, end, length = map(int, sys.stdin.readline().rstrip().split())
    if end > d:
        continue
    highway[start].append((end, length))
dijkstra(0)
print(distance[d])
