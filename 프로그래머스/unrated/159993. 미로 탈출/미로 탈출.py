from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    s, e, l = (-1,-1),(-1,-1),(-1,-1)
    isDecided = False
    for r in range(R):  # 시작, 출구, 레버의 위치를 파악한다
        for c in range(C):
            if maps[r][c] == 'S':
                s = (r,c)
            elif maps[r][c] == 'E':
                e = (r,c)
            elif maps[r][c] == 'L':
                l = (r,c)
            if s != (-1,-1) and e != (-1,-1) and l != (-1,-1):
                isDecided = True
                break
        if isDecided:
            break
            
    def bfs(sr, sc, er, ec):
        dq = deque()
        dq.append((sr,sc))
        visited = [[-1]*C for _ in range(R)]
        visited[sr][sc] = 0
        while dq:
            r, c = dq.popleft()
            if r==er and c==ec:
                break
            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=nr<R and 0<=nc<C and visited[nr][nc]==-1 and maps[nr][nc]!='X':
                    visited[nr][nc] = visited[r][c] + 1
                    dq.append((nr,nc))
        return visited[er][ec]

    sl, le = bfs(*s,*l), bfs(*l,*e)
    # 시작부터 레버까지의 거리, 레버부터 출구까지의 거리. 도달할 수 없다면 -1
    return -1 if sl==-1 or le==-1 else sl+le