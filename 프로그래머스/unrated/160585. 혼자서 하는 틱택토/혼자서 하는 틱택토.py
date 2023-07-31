from collections import deque

def solution(board):
    
    def bfs(i,j):
        nonlocal winner
        move = ((0,1),(1,1),(1,0),(1,-1))
        pos = []
        for m in range(4):
            ni, nj = i+move[m][0],j+move[m][1]
            if 0<=ni<3 and 0<=nj<3 and board[i][j] == board[ni][nj]:
                pos.append((ni,nj,m))   # 위치, 방향
        for p in pos:
            i, j, m = p
            ni, nj = i+move[m][0],j+move[m][1]
            if 0<=ni<3 and 0<=nj<3 and board[i][j] == board[ni][nj]:
                if winner=='':
                    winner = board[i][j]
                elif winner != board[i][j]:
                    return 0
        return 1
                    
    o_cnt = 0    # O와 X의 개수를 센다
    x_cnt = 0
    winner = ''       # 승자
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O': 
                o_cnt += 1
            elif board[i][j] == 'X': 
                x_cnt += 1 
            if (i == 0 or j == 0) and board[i][j]!='.':
                if bfs(i,j) == 0:
                    return 0

    if o_cnt - x_cnt < 0 or o_cnt - x_cnt > 1:
        return 0
    if winner=='O' and o_cnt - x_cnt != 1:
        return 0
    if winner=='X' and o_cnt - x_cnt != 0:
        return 0
    
    return 1