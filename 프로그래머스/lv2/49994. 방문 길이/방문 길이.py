def solution(dirs):
    move = set()
    D = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
    r, c = 0, 0
    for dir in dirs:
        dr, dc = D[dir]
        nr, nc = r+dr, c+dc
        if -5<=nr<=5 and -5<=nc<=5:
            if (r,c,nr,nc) not in move and (nr,nc,r,c) not in move:
                move.add((r,c,nr,nc))
            r, c = nr, nc
    return len(move)