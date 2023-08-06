import heapq

def solution(n, works):
    works = list(map(lambda x:-x, works))
    heapq.heapify(works)
    
    for _ in range(n):
        work = heapq.heappop(works)
        if work == 0: break     # 최대값이 0이면 중지
        heapq.heappush(works,work+1)
    
    return sum(map(lambda x:x*x, works))