def solution(park, routes):
    R, C = len(park), len(park[0])
    now = (-1,-1)
    for r in range(R):
        for c in range(C):
            if park[r][c]=='S':
                now = (r,c)
                break
        if now != (-1,-1):
            break
    
    move = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    for route in routes:
        dir, cnt = route.split()
        r, c = now[0], now[1]
        blocked = False
        for _ in range(int(cnt)):
            r += move[dir][0]
            c += move[dir][1]
            if 0<=r<R and 0<=c<C and park[r][c] == 'X':
                blocked = True
                break
        if 0<=r<R and 0<=c<C and not blocked:
            now = (r,c)
            
    return now