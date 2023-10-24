import heapq

def solution(jobs):    
    hq = []
    now, idx, answer, start = 0, 0, 0, -1

    while idx < len(jobs):
        for req, time in jobs:
            if start < req <= now:
                heapq.heappush(hq, (time, req))
        if hq:
            time, req = heapq.heappop(hq)
            start = now
            now += time
            answer += now - req
            idx += 1
        else:
            now += 1
    
    return answer//len(jobs)