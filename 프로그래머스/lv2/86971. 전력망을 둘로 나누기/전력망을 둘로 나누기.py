from collections import deque

def solution(n, wires):
    def bfs(n):
        connected = {n}
        q = deque([n])
        while q:
            now = q.popleft()
            for nc in graph[now]:
                if nc not in connected:
                    connected.add(nc)
                    q.append(nc)
        return len(connected)
    
    lw = len(wires)
    answer = n
    for i in range(lw):
        graph = [[] for _ in range(n+1)]
        for j in range(lw):
            if i==j:
                continue
            wire = wires[j]
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
        answer = min(answer, abs(n-bfs(1)*2))  
    return answer