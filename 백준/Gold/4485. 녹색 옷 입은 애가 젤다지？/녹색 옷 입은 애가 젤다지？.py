import heapq

def dijkstra(i, j):
    global cave, N
    money = [[float('inf')]*N for _ in range(N)]
    money[i][j] = cave[i][j]
    q = []
    heapq.heappush(q, (money[i][j],i,j))
    while q:
        ij_money,i,j= heapq.heappop(q)
        if i==N-1 and j==N-1:
            return ij_money
        if money[i][j]<ij_money:
            continue
        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                new_money = ij_money+cave[ni][nj]
                if new_money < money[ni][nj]:
                    heapq.heappush(q, (new_money,ni,nj))
                    money[ni][nj] = new_money
        
case = 1
while True:
    N = int(input())
    if N == 0:
        break
    cave = [tuple(map(int,input().split())) for _ in range(N)]
    print(f'Problem {case}: {dijkstra(0,0)}')
    case += 1