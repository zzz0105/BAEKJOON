from collections import deque
def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])  # 세로, 가로
    visited = [[False]*M for _ in range(N)]
    
    def bfs(i,j):
        nonlocal visited
        dq = deque()
        dq.append((i,j))
        visited[i][j] = True
        food = int(maps[i][j])
        while dq:
            i, j = dq.popleft()
            for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M and maps[ni][nj]!="X" and not visited[ni][nj]:
                    dq.append((ni,nj))
                    visited[ni][nj] = True
                    food += int(maps[ni][nj])
        return food
    
    for i in range(N):
        for j in range(M):
            if maps[i][j]!="X" and not visited[i][j]:
                answer.append(bfs(i,j))
                
    return [-1] if not answer else sorted(answer)