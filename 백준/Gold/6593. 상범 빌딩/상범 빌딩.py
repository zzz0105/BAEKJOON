from collections import deque

move = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))

def bfs(l,r,c):
    dq = deque()
    dq.append((l,r,c))
    floor[l][r][c] = 0
    while dq:
        l,r,c = dq.popleft()
        if (l,r,c) == coord_e:
            return floor[l][r][c]
        for dl,dr,dc in move:
            nl,nr,nc = l+dl,r+dr,c+dc
            if 0<=nl<L and 0<=nr<R and 0<=nc<C and floor[nl][nr][nc] in {'E','.'}:
                dq.append((nl,nr,nc))
                floor[nl][nr][nc] = floor[l][r][c] + 1
    return -1    

while True:
    L, R, C = map(int,input().split())
    if L == R == C == 0:
        break
    coord_s, coord_e = (), ()
    floor = [[[] for _ in range(R)] for _ in range(L)]
    for l in range(L):
        for r in range(R):
            floor[l][r] = list(input())
            if coord_s == () or coord_e == ():
                for c in range(C):
                    if floor[l][r][c] == 'S':
                        coord_s = (l,r,c)
                    elif floor[l][r][c] == 'E':
                        coord_e = (l,r,c)
        input()

    answer = bfs(*coord_s)
    print('Escaped in '+ str(answer) +' minute(s).' if answer!=-1 else 'Trapped!')