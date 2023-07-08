from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def bfs(c):
        nonlocal visited  
        dq = deque([c])
        while dq:
            c = dq.popleft()
            for j in range(n):
                if computers[c][j]==1 and not visited[j]:
                    dq.append(j)
                    visited[j] = True
        return 1
            
    for i in range(n):
        if not visited[i]:  answer += bfs(i)
        
    return answer