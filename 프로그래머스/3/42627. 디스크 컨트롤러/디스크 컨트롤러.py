import heapq

def solution(jobs):
    hq = []
    req_end = []
    now = 0
    for request, duration in jobs:
        heapq.heappush(hq, [duration,request])

    while hq:
        duration, request = heapq.heappop(hq)
        req_end.append(max(0, now-request) + duration)
        now = duration + max(now,request)

    return sum(req_end)//len(jobs)