def check(x, y, n):
    global video
    tmp = video[x][y]
    for i in range(n):
        for j in range(n):
            if tmp != video[x+i][y+j]:
                return False
    return True

def div(x, y, n):
    global video
    if check(x, y, n):
        print(video[x][y],end='')
        return 
    else:
        print('(',end='')
        n //= 2
        div(x, y, n)
        div(x, y+n, n)
        div(x+n, y, n)        
        div(x+n, y+n, n)
        print(')', end="")

n = int(input())
video = [list(input()) for _ in range(n)]
div(0,0,n)