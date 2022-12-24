import sys, heapq
input = sys.stdin.readline

N, Hc, T = map(int,input().split())
H = []
answer = 'NO'
for _ in range(N):
    h = int(input())
    heapq.heappush(H, -h)

h = -heapq.heappop(H)
heapq.heappush(H, -h)
if h < Hc:
    answer = 'YES'
    i = 0
else:
    for i in range(1, 1+T):
        h = int(-heapq.heappop(H)/2)
        if h == 0:
            h = 1
        heapq.heappush(H, -h)
        h = int(-heapq.heappop(H))
        if h < Hc:
            answer = 'YES'
            break
        heapq.heappush(H, -h)

if answer == 'YES':
    print('YES')
    print(i)
else:
    print('NO')
    print(-heapq.heappop(H))