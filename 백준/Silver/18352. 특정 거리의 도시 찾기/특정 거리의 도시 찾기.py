import heapq, sys

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in cities[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n, m, k, x = map(int,sys.stdin.readline().rstrip().split())
cities = [[] for _ in range(n+1)]
distance = [float('inf')]  * (n+1)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    cities[a].append((b,1))
dijkstra(x)

answer = []
for i in range(len(distance)):
    if distance[i] == k:
        answer.append(i)
if answer:
    print(*answer, sep='\n')
else:
    print(-1)
