import sys, heapq

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    max_h = []
    min_h = []
    visited = [False]*k
    for i in range(k):
        o, n = sys.stdin.readline().rstrip().split()
        if o == 'I':
            # max_h와 min_h 동기화시 요소를 구분할 때 i를 사용한다 
            heapq.heappush(max_h, (-int(n), i))
            heapq.heappush(min_h, (int(n), i))
            visited[i] = True
        else:
            if n == '1':    # 최댓값 삭제
                # visited[i]로 min_h에서 이미 삭제된 요소인지 판단
                # 이미 삭제된 요소라면(visited[i]==False) 삭제되지 않은 요소가 나올 때까지 모두 삭제
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            else:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)
    
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)

    if max_h and min_h:
        print(heapq.heappop(max_h)[0]*-1, heapq.heappop(min_h)[0]) 
    else:
        print('EMPTY')