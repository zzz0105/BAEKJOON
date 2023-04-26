def check(r):
    for tr in range(r):
        if board[tr]==board[r] or abs(board[tr]-board[r])==abs(tr-r):
            return False
    return True

def bt(r):
    global cnt
    if r==N:
        cnt += 1
        return
    for c in range(N):
        board[r] = c
        if check(r):
            bt(r+1)

N = int(input())
cnt = 0
board = [0]*N
bt(0)
print(cnt)